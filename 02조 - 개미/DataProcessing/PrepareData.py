
# %%
from textblob import TextBlob
import pandas as pd
import datetime as dt
import numpy as np
import re
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# %%
def concat_twitter_dat(path, search_word, start_date, last_date):
    results = pd.DataFrame([])
    for date in pd.date_range(start=start_date, end=last_date):
        results = results.append(pd.read_csv(path +
                                            search_word +
                                            "_" +
                                            date.strftime('%Y-%m-%d') + ".csv", index_col=0, parse_dates=["date"]))
    return results.reset_index(drop=True)

def cleanUpTweet(txt):
    txt = re.sub(r'@[A-Za-z0-9_]+', '', txt)
    txt = re.sub(r'#', '', txt)
    txt = re.sub(r'RT : ', '', txt)
    txt = re.sub(r'https?:|/|/[A-Za-z0-9\.\/]+', '', txt)
    return txt


def convertDateType(stock_data):
    results = stock_data.copy()
    results["Date"] = results.index.tz_convert('UTC')
    results["Date"] = results["Date"].dt.tz_localize(None)
    results = results.reset_index(drop=True)
    return results


def makePersent(data):
    result = data.copy()
    for i in range(1,data.shape[0]):
        result.loc[i,"Open"]=(data.loc[i,"Open"]-data.loc[i-1,"Close"])/data.loc[i-1,"Close"] *100
        result.loc[i,"High"]=(data.loc[i,"High"]-data.loc[i-1,"Close"])/data.loc[i-1,"Close"] *100
        result.loc[i,"Low"]=(data.loc[i,"Low"]-data.loc[i-1,"Close"])/data.loc[i-1,"Close"] *100
        result.loc[i,"Close"]=(data.loc[i,"Close"]-data.loc[i-1,"Close"])/data.loc[i-1,"Close"] *100
        result.loc[i,"Adj Close"]=(data.loc[i,"Adj Close"]-data.loc[i-1,"Adj Close"])/data.loc[i-1,"Adj Close"] *100
        
        result.loc[i,"Volume"]=(data.loc[i,"Volume"]-data.loc[i-1,"Volume"])/data.loc[i-1,"Volume"] *100
        
    return result
        
    

# %%
def getTextSubjectivity(txt):
    return TextBlob(txt).sentiment.subjectivity

def getTextPolarity(txt):
    return TextBlob(txt).sentiment.polarity

def getTextAnalysis(a):
    if a < 0:
        return "Negative"
    elif a == 0:
        return "Neutral"
    else:
        return "Positive"

def emotiontDataAdd(twitter_data):
    results = twitter_data.copy()
    results['clean_text'] = results['text'].apply(cleanUpTweet)
    results["polarity"] = results['clean_text'].apply(getTextPolarity)
    results["subjectivity"] = results['clean_text'].apply(getTextSubjectivity)
    results["emotion"] = results['polarity'].apply(getTextAnalysis)
    return results

# %%
def addAndSelectFeature(stock_data,
                         twitter_data,
                         tweet_lag=60,
                         subset_tweets_per=1):

    interval = int((stock_data["Date"][1] - stock_data["Date"][0]).seconds / 60)
    

    results = stock_data.copy()
    results["tw_count"] = pd.NA     # number of tweets per interval
    # results["tw_mean"] = pd.NA      # mean of number of tweets per subset_twets_per in interval
    # results["tw_vola"] = pd.NA      # volatility of number of tweets per subset_tweets_per in interval
    # results["tw_min"] = pd.NA       # min number of tweets per subset_tweets_per in interval
    # results["tw_max"] = pd.NA       # max number of tweets per subset_tweets_per in interval
    results["tw_pola"] =pd.NA      # avg polarity of tweets
    results["tw_subj"] = pd.NA     # avg subjectivity of tweets
    results["tw_n_pos"] = pd.NA     # number of positive tweets
    results["tw_n_neg"] = pd.NA     # number of negative tweets
    results["tw_ratio_pos"] =pd.NA # share of positive tweets
    results["tw_ratio_neg"] = pd.NA # share of negative tweets
    

    for i in range(0, stock_data.shape[0]):
        current_time = stock_data.loc[i,"Date"]
        
        cond_1 = twitter_data["date"] < (current_time + dt.timedelta(minutes=interval - tweet_lag))
        cond_2 = twitter_data["date"] >= (current_time - dt.timedelta(minutes=tweet_lag))
        
        twitter_subset = twitter_data.loc[cond_1 & cond_2, :].copy().reset_index(drop=True)
        
        results.loc[i, "tw_count"] = twitter_subset.shape[0]
        

        tweets_per = pd.Series(np.zeros(interval))
        for x in np.arange(subset_tweets_per, interval + 1, subset_tweets_per):
            sub_cond_1 = twitter_subset["date"] >= (current_time + dt.timedelta(minutes=(int(x) - 1 - tweet_lag)))
            sub_cond_2 = twitter_subset["date"] < (current_time + dt.timedelta(minutes=(int(x) - tweet_lag)))
            tweets_per[x - 1] = twitter_subset.loc[sub_cond_1 & sub_cond_2, :].shape[0]
            
        # Compute Variables "tw_mean", "tw_vola", "tw_min", "tw_max"
        # results.loc[i, "tw_mean"] = tweets_per.mean()
        # results.loc[i, "tw_vola"] = tweets_per.var()
        # results.loc[i, "tw_min"] = tweets_per.min()
        # results.loc[i, "tw_max"] = tweets_per.max()
        

        # Content related variables
        results.loc[i, "tw_pola"] = twitter_subset["polarity"].mean()
        results.loc[i, "tw_subj"] = twitter_subset["subjectivity"].mean()
        results.loc[i, "tw_n_pos"] = twitter_subset.loc[twitter_subset.emotion == "Positive", :]
        results.loc[i, "tw_n_neg"] = twitter_subset.loc[twitter_subset.emotion == "Negative", :]
        if twitter_subset.shape[0]!=0:
            results.loc[i, "tw_ratio_pos"] = results.loc[i, "tw_n_pos"] / twitter_subset.shape[0]
            results.loc[i, "tw_ratio_neg"] = results.loc[i, "tw_n_neg"] / twitter_subset.shape[0]
        
    return results

# %%
def getPreaparedData(stock_name,start_date,last_date):
    path="./data"
    search_word=stock_name


    concat_data=concat_twitter_dat(path,search_word,start_date,last_date)

    cleand_data=concat_data
    cleand_data["text"]=concat_data["text"].apply(cleanUpTweet)


    prepare_data=emotiontDataAdd(cleand_data)
    prepare_data["date"]=prepare_data["date"].dt.tz_localize(None)


    interval="1D"
    stock_data=pd.read_csv(path +"stock_" + start_date + "_" + last_date  + "_"+ interval + ".csv")
    stock_data["Date"]=pd.to_datetime(stock_data["Date"],utc=True)
    stock_data.set_index('Date',drop=False, inplace=True)
    stock_data=convertDateType(stock_data)

    variables_data=addAndSelectFeature(stock_data,prepare_data)
    variables_data=variables_data.fillna(0)
    variables_data=variables_data.drop(["Date"],axis=1)


    persent_data_data=makePersent(variables_data)
    # first volume of yfinace data is always 0. so second volume persent is inf. remove two row
    #sometimes last row have current date. not target date
    variables_data=persent_data_data.drop([persent_data_data.index[0]],axis=0)
    variables_data=variables_data.drop([variables_data.index[0]],axis=0)
    variables_data=variables_data.drop([variables_data.index[-1]],axis=0)
    variables_data=variables_data.reset_index(drop=True)


    scaler = MinMaxScaler()
    variables_data[["tw_count"]]=scaler.fit_transform(variables_data[["tw_count"]])
    only_stock_data_training = variables_data.iloc[:, 0:6].copy()

    train_set, test_set = train_test_split(variables_data, test_size = 0.3,shuffle=False)
    only_stock_train_set, only_stock_test_set = train_test_split(only_stock_data_training, test_size = 0.3,shuffle=False)
    return train_set, test_set, only_stock_train_set, only_stock_test_set


def makeLSTMDataSet(data_training,data_test
                    ,step_size = 5):
    train_data = []
    target_data = []

    for i in range(step_size, data_training.shape[0]):
        train_data.append(data_training.loc[i - step_size:i-1])
        target_data.append(data_training.loc[i, "Close"])
    train_data, target_data = np.array(train_data), np.array(target_data)

    #test data
    test_train_data = []
    test_target_data = []
    
    data_test=data_test.reset_index(drop=True)
    for i in range(step_size, data_test.shape[0]):
        test_train_data.append(data_test.loc[i - step_size:i-1])
        test_target_data.append(data_test.loc[i, "Close"])
    test_train_data, test_target_data = np.array(test_train_data), np.array(test_target_data)
    
    return train_data, target_data, test_train_data, test_target_data
