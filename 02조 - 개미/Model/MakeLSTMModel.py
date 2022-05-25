#  Create  Model
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from keras.callbacks import EarlyStopping
from keras_tuner.tuners import RandomSearch
import tensorflow as tf
import keras.backend as K
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras
from keras.callbacks import ModelCheckpoint

def model_wrapper_get_input_size(input_data):
    def build_model(hp):
        model = Sequential()
        
        hidden = hp.Int("num_layers",
                    min_value = 0,
                    max_value = 3)
        activations = hp.Choice("activation",
                                        values = ["relu", "tanh", "sigmoid"],
                                        default = "relu")
        model.add(LSTM(units = hp.Int("units",
                                    min_value = 18,
                                    max_value = 128,
                                    step = 32),
                    activation = activations,
                    input_shape = (input_data.shape[1], input_data.shape[2]),
                    return_sequences = True if hidden > 0 else False))
        
        if hidden > 0:
            for layer in range(hidden):
                model.add(Dropout(hp.Float("dropout_hidden" + str(layer + 1),
                                        min_value = 0.1,
                                        max_value = 0.9,
                                        step = 0.1)))
                
                model.add(LSTM(units = hp.Int("units_hidden" + str(layer + 1),
                                            min_value = 18,
                                            max_value = 64,
                                            step = 32),
                            activation = activations,
                            return_sequences = True if layer+1 != hidden else False))
                
        model.add(Dropout(hp.Float("dropout",
                                min_value = 0.1,
                                max_value = 0.9,
                                step = 0.1)))
        model.add(Dense(units = 1))
        
        hp_learning_rate = hp.Choice('learning_rate', values = [1e-2, 1e-3, 1e-4]) 
        model.compile(optimizer = keras.optimizers.Adam(learning_rate = hp_learning_rate),
                        loss = 'mean_squared_error')
            
        return model
    return build_model

def getBestModel(trainData,targetData,projectName="recommend_stock"):
    tuner = RandomSearch(model_wrapper_get_input_size(trainData),
                        objective = 'loss',
                        max_trials = 10,
                        executions_per_trial = 2,
                        overwrite=False,
                        directory = "model_store",
                        project_name=projectName,)




    early_stopping_cb = EarlyStopping(monitor='loss',patience = 10)

    tuner.search(trainData,
                targetData,
                epochs = 100,
                batch_size = 32,
                validation_split = 0.2,
                callbacks = [early_stopping_cb])

    best_hps = tuner.get_best_hyperparameters(num_trials = 1)[0]



    best_model = tuner.hypermodel.build(best_hps)

    print(f"""
    The hyperparameter search is complete. The optimal number of units in the first densely-connected
    layer is {best_hps.get('units')} and the optimal learning rate for the optimizer
    is {best_hps.get('learning_rate')}.
    """)
    return best_model