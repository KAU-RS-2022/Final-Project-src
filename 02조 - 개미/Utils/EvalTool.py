
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error
from keras.models import load_model

def accOfUpDown(pred,real):
    #if same sign, multiply num is positive num
    isSame=pred*real
    isSame=isSame[isSame>0]
    return isSame.shape[0]/pred.shape[0]*100

def virtual_invest(pred,real):
    money=100
    isHave=False
    
    for i in range(0,pred.shape[0]):
        
        if money<0:
            return money
        
        if pred[i]<0:
            if(isHave):
                isHave=False
            else:
                pass
            
        elif pred[i]>0:
            if(isHave):
                money=money+money*real[i]/100
            else:
                isHave=True
                money=money+money*real[i]/100
    

    return money
def plotXY(pred,real):
    plt.figure(figsize = (20, 10))
    plt.plot(pred)
    plt.plot(real)
    plt.title('Prediction vs Real Stock')
    plt.ylabel('ups and downs')
    plt.xlabel('Days')
    plt.legend(['Prediction', 'Real'], loc='best')
    
def printEval(model_name,test_target_data,test_train_data):
    saved_model = load_model(model_name, compile = False)
    print(saved_model)

    predict_test_train_data = saved_model.predict(test_train_data)
    predict_test_train_data = predict_test_train_data.flatten()

    error_lstm = mean_squared_error(test_target_data, predict_test_train_data)
    print("MSE Error is", error_lstm)

    upDownAcc=accOfUpDown(predict_test_train_data,test_target_data)
    print(upDownAcc,"%")

    virtual_money=virtual_invest(predict_test_train_data,test_target_data)
    print(virtual_money,"$")

    plotXY(predict_test_train_data,test_target_data)
