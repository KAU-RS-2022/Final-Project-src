import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')

from gensim.models.phrases import Phrases, Phraser
from gensim.models import Word2Vec

from sklearn.cluster import KMeans

import os
import warnings
warnings.filterwarnings('ignore')

import multiprocessing



def load_data():
    file_dir = './data'
    df = pd.DataFrame()

    # 디렉토리에서 트윗 파일 불러오기
    for file_name in os.listdir(file_dir):
        # 트윗 파일이 아니면 넘김
        #if ('PLTR' not in file_name) and ('palantir' not in file_name):
        if 'stock' in file_name:
            print(f"FIle skipped (not tweet): {file_name}")
            continue

        file_path = os.path.join(file_dir, file_name)

        # 트윗 파일 로드 및 병합
        try:
            file = pd.read_csv(file_path, index_col=0)
            if len(file) == 0:
                continue
            df = df.append(file)

        except Exception as error_message:
            print(f'error: {error_message}')

            
    # 인덱스 초기화
    df = df.reset_index(drop=True)
    df = df.rename(columns={'text':'tweet'})


    # 중복 트윗 제거, 내용이 없는 트윗 제거
    df = df.drop_duplicates(subset='tweet', keep='first')
    df = df.dropna(subset=['tweet', 'likes'])
    
    return df


def clean_tweet(tweet):
    lemma = WordNetLemmatizer()
    stop_words = stopwords.words("english")
    
    tweet = str(tweet)
    tweet = tweet.lower() # 소문자로 바꾸기
    tweet = re.sub('https?:\/\/[a-zA-Z0-9@:%._\/+~#=?&;-]*', ' ', tweet) # URL 제거
    tweet = re.sub('\$[a-zA-Z0-9]*', ' ', tweet) # ticker symbol($로 시작하는 주식 관련 심볼) 제거
    tweet = re.sub('\@[a-zA-Z0-9]*', ' ', tweet) # 유저 호출하는 기능(@로 시작) 제거
    tweet = re.sub('[^a-zA-Z\']', ' ', tweet) # 문자가 아닌 것 제거
    tweet = ' '.join( [w for w in tweet.split() if len(w)>1] )
    
    tweet = ' '.join([lemma.lemmatize(x) for x in nltk.wordpunct_tokenize(tweet) if x not in stop_words])
    tweet = [lemma.lemmatize(x, nltk.corpus.reader.wordnet.VERB) for x in nltk.wordpunct_tokenize(tweet) if x not in stop_words]
    
    return tweet 


def preprocess_data(df):
    # 트윗을 토큰화시킨 것, 그리고 토큰을 이어붙인 것을 새로운 열에 추가
    df["clean_tweet"] = df["tweet"].apply(lambda x:clean_tweet(x))
    df["cleaned_tweet"] = df["clean_tweet"].apply(lambda x:' '.join(x))

    # 날짜를 DateTime으로 변환하고, 월/년도 열을 추가
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    
    return df


def find_label(df):
    # clean_tweet 열을 embedding이 지원하는 형식으로 변환
    sent = [row for row in df["clean_tweet"]]

    # Gensim의 Pharases 패키지를 이용하여 자동으로 common pharases (bigrams)을 찾기
    phrases = Phrases(sent, min_count=1, progress_per=50000)
    bigram = Phraser(phrases)
    sentences = bigram[sent]
    
    return sentences


def train_w2v_model(sentences):
    w2v_model = Word2Vec(min_count=4,
                         window=20,
                         vector_size=300,
                         #sample=1e-5,
                         alpha=0.03, 
                         min_alpha=0.0007,
                         negative=20,
                         seed=42,
                         workers=multiprocessing.cpu_count()-1)


    # 위에서 찾은 common pharases를 이용하여 Word2Vec model의 vocab 만들기
    w2v_model.build_vocab(sentences, progress_per=50000)
    
    # Word2Vec training 시작
    w2v_model.train(sentences, total_examples=w2v_model.corpus_count, epochs=50, report_delay=1)
    
    # 모델 결과 저장
    w2v_model.save("word2vec.model")
    word_vectors = Word2Vec.load("word2vec.model").wv
    
    return word_vectors


# K-means clustering을 위해 Word2Vec 모델의 결과(단어의 embedding)를 변수에 불러오기
def train_KMeans_model(word_vectors):
    # 단어를 positive, negative, neutral 3가지로 군집화하기 위해 KMeans model에 embedding을 입력
    KM_model = KMeans(n_clusters=3, n_init=20, max_iter=1000, init='k-means++', random_state=42).fit(X=word_vectors.vectors.astype('double'))
    
    return KM_model


# 단어별로 embedding과 label을 기록하여 DataFrame을 만들기
def get_df_words(word_vectors, KM_model):
    words = pd.DataFrame(word_vectors.index_to_key)
    words.columns = ['words']
    words['vectors'] = words.words.apply(lambda x: word_vectors[f'{x}'])
    words['cluster'] = words.vectors.apply(lambda x: KM_model.predict([np.array(x)]))
    words.cluster = words.cluster.apply(lambda x: x[0])

    # cluster_value 열을 추가하고 positive면 1, neutral이면 0, negative면 -1을 기록
    words['cluster_value'] = [-1 if i==2 else 1 if i==0 else 0 for i in words.cluster]

    # 군집으로부터 얼마나 근접해있는지 기록
    words['closeness_score'] = words.apply(lambda x: 1/(KM_model.transform([x.vectors]).min()), axis=1)
    
    return words


def get_words_dict(words):
    # {'단어':'cluster_value'} 형태의 dictionary 생성
    words_dict = dict(zip(words.words, words.cluster_value))
    
    return words_dict


def get_dictionary():
    df = load_data()
    df = preprocess_data(df)
    
    sentences = find_label(df)
    word_vectors = train_w2v_model(sentences)
    KM_model = train_KMeans_model(word_vectors)
    
    df_words = get_df_words(word_vectors, KM_model)
    words_dict = get_words_dict(df_words)
    
    return words_dict


def get_sentiments(tweet, sent_dict):
    total_sentiment = 0
    word_count = 0
    avg = 0
    words = clean_tweet(tweet)
    for word in words:
        if sent_dict.get(word):
            total_sentiment += int(sent_dict.get(word))
        word_count += 1
    
    if word_count != 0:
        avg = total_sentiment / word_count
    
    # 평균값이 0.15 미만이면 negative, 0.15 초과면 positive, 그 외는 neutral (수치는 임의로 설정)
    sentiment = -1 if avg < -0.15 else 1 if avg > 0.15 else 0
    
    return sentiment