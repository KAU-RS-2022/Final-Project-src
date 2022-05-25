import sys
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mplcursors # Use this is for creating a cursor-interactive plot with "%matplotlib notebook"
from sklearn.decomposition import NMF # Use this for training Non-negative Matrix Factorization
from sklearn.utils.extmath import randomized_svd # Use this for training Singular Value Decomposition
from sklearn.manifold import TSNE # Use this for training t-sne manifolding

def rs(userNumber):
    pd.set_option('display.max_rows', None)

    plt.style.use('ggplot') # You can also use different style

    # just for plot checking, use this option
    # %matplotlib inline
    # for interactive plot
    # If you use this option, plot will appear at first-drawn position
    # %matplotlib notebook

    warnings.filterwarnings('ignore')

    dir = './recipe/'
    df_ratings = pd.read_csv(dir + 'rating_50000.csv', usecols=["user_id","rcp_sno","rating"])# for title-matching
    df_lists = pd.read_csv(dir + 'recipe_list.csv', usecols=["rcp_sno","ckg_nm","inq_cnt","rcmm_cnt","srap_cnt","ckg_mth_acto_nm","ckg_sta_acto_nm","ckg_knd_acto_nm","ckg_mtrl_acto_nm","ckg_mtrl_cn","ckg_inbun_nm","ckg_dodf_nm","ckg_time_nm"]) 


    # 고유 사용자, 고유 레시피 갯수 확인
    n_users = len(df_ratings["user_id"].unique())
    n_recipes = len(df_ratings["rcp_sno"].unique())

    n_users, n_recipes # 100 명의 사용자가 5122개의 레시피에 평점을 매김을 확인

    len(df_lists) # len(df_lists) - n_lists 만큼의 평점이 매겨지지 않은 레시피가 존재

    # ratings의 기술통계량 확인
    df_ratings["rating"].describe()

    #unrated 레시피목록
    set(df_lists['rcp_sno'].unique())-set(df_ratings['rcp_sno'].unique())


    # your code here
    data=np.zeros((n_recipes,n_users))
    A = df_ratings.set_index(["rcp_sno", "user_id"]).unstack().fillna(0).to_numpy()

    # 올바른 형태로 utility matrix가 생성되었는지 확인
    # print(A.shape)

    # your code here
    A = np.asarray(A)
    k = 50
    U, Sigma, VT = randomized_svd(A, n_components=k)

    # 분해된 행렬이 올바른 형태로 생성되었는지 확인
    # print(U.shape, Sigma.shape, VT.shape) #(n_movies, k), (k,) (k, n_users)

    Sigma_mat = np.diag(Sigma)
    A_approx_svd = np.dot(np.dot(U, Sigma_mat), VT)


    # 근사 행렬이 올바른 형태로 생성되었는지 확인
    # print(A_approx_svd.shape) 



    k = 50
    A = np.asarray(A)
    model_nmf = NMF(n_components=k, init='random', random_state=0)
    W = model_nmf.fit_transform(A)
    H = model_nmf.components_

    # 분해된 행렬이 올바른 형태로 생성되었는지 확인
    # print(W.shape, H.shape)

    A_approx_nmf = np.dot(W,H)

    # 근사 행렬이 올바른 형태로 생성되었는지 확인
    # print(A_approx_nmf.shape) 


    from sklearn.metrics import mean_squared_error

    def compute_error(actual, prediction):

        
        prediction = prediction[np.nonzero(actual)]
        actual = actual[np.nonzero(actual)]
    
        
        
        sse = np.sum((actual-prediction)**2)
        rmse = np.sqrt(sse*(1/len(actual)))
        

        
        
        return sse, rmse

    def compute_error_all(actual, prediction):
    #     actual=np.asarray(actual)
    #     prediction = np.asarray(prediction)
    #     prediction = prediction.flatten()
    #     actual = actual.flatten()
    #     print(len(actual))
        
    #     print(actual.shape, prediction.shape)
        
        # actual 행렬 안의 0값을 갖는 원소들도 포함해서 오차를 계산합니다.
        sse = np.sum((actual-prediction)**2)
        rmse = np.sqrt(sse*(1/len(actual)))        
        
        return sse, rmse


    # print(f"SVD Error(ignoring zero values): SSE = {compute_error(A, A_approx_svd)[0]}, RMSE = {compute_error(A, A_approx_svd)[1]}")
    # print(f"NMF Error(ignoring zero values): SSE = {compute_error(A, A_approx_nmf)[0]}, RMSE = {compute_error(A, A_approx_nmf)[1]}")

    # print('\n')

    # print(f"SVD Error(including all zero values): SSE = {compute_error_all(A, A_approx_svd)[0]}, RMSE = {compute_error_all(A, A_approx_svd)[1]}")
    # print(f"NMF Error(including all zero values): SSE = {compute_error_all(A, A_approx_nmf)[0]}, RMSE = {compute_error_all(A, A_approx_nmf)[1]}")

    def makePredictions(actual, pred, user):
        pd.set_option('display.max_seq_items', None)
        pd.set_option('display.max_rows', None)

        pred = pd.DataFrame(data =pred , index=actual.index, columns = actual.columns)
    
        

        pred.index.name="rcp_sno"
        
        rated_recipes = actual[actual[user]!=0.0][user]
    
        unrated_recipes = pred[user]
        
        
        rated_movies = actual.loc[actual.notnull()[user],:][user]
        unrated_movies = pred.loc[actual.isnull()[user],:][user]
        
        con_1 = pd.merge(df_lists, rated_recipes, left_on='rcp_sno',right_index=True, how='outer')
    
        con = pd.merge(con_1, unrated_recipes, left_on='rcp_sno',right_index=True, how='outer')

        


        

        con.columns =["rcp_sno","ckg_nm","inq_cnt","rcmm_cnt","srap_cnt","ckg_mth_acto_nm","ckg_sta_acto_nm","ckg_knd_acto_nm","ckg_mtrl_acto_nm","ckg_mtrl_cn","ckg_inbun_nm","ckg_dodf_nm","ckg_time_nm","rating","prediction"]
        unrated_movies = unrated_movies[actual[user]==0.0]
        
        
        
        allList = (actual[actual[user]!=0.0][user]).index.tolist()
        # print(len(allList))
        unrated_recipes = con[~con['rcp_sno'].isin(allList)]
        # con = con.drop(['rcp_sno'], axis=1)
        rated_recipes= con.sort_values(by=['rating'], axis=0, ascending=False)
        # unrated_recipes = unrated_recipes.drop(['rcp_sno'], axis=1)
        
        
        unrated_recipes=unrated_recipes.sort_index(axis=0)
        
    
        
        

        
        return rated_recipes, unrated_recipes


    def findMiddle(dataframe):
        # dataframe의 중간 부분을 반환하는 함수입니다.
        # return은 dataframe의 중간 10개 부분들 입니다. (dataframe 형식)
        n_idx = int(len(dataframe.index)/2)
        # print(len(dataframe.iloc[n_idx-5:n_idx+5]))
        return dataframe.iloc[n_idx-5:n_idx+5]
            

    A= df_ratings.pivot_table('rating',index='rcp_sno', columns='user_id').fillna(0)


    prediction_with_rated_svd, prediction_with_unrated_svd = makePredictions(A, A_approx_svd, userNumber) # 실제 Utility Matrix와 svd를 통해 근사한 행렬 간의 비교
    prediction_with_rated_nmf, prediction_with_unrated_nmf = makePredictions(A, A_approx_nmf, userNumber) # 실제 Utility Matrix와 nmf를 통해 근사한 행렬 간의 비교

    prediction_with_rated_svd = prediction_with_rated_svd.sort_values('prediction', ascending=False)[['rcp_sno','rating','prediction']]
    prediction_with_rated_nmf = prediction_with_rated_nmf.sort_values('prediction', ascending=False)[['rcp_sno','rating','prediction']]

    rated_svd_val = prediction_with_rated_svd.values

    result = str(rated_svd_val[:50]).replace(' [','').replace('[[','').replace(']','');
    print(result);

    # for i in range(10):
    #     print(rated_svd_val[i][0]);
    #     print(rated_svd_val[i][1]);
    #     print(rated_svd_val[i][2]);

    # print(prediction_with_rated_svd);
    # print(prediction_with_rated_nmf);

def test(user):
    print(user);
    print(type(user));

if __name__ == '__main__':
    user = sys.argv[1]  #user number 숫자 들어감 현재 1~100 사이
    rs(int(user));
    # test(user);