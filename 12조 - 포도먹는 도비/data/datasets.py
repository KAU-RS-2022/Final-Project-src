# coding=<utf-8>
import os
import glob
import numpy as np
import pandas as pd
import pickle

import torch
from torch.utils import data
import torch.distributed as dist
from functools import lru_cache

# from utils import transform

'''
data loader for wine recommendation
'''


class WineDataSet(data.Dataset):
    # @lru_cache(maxsize=None)
    def __init__(self):
        '''
        path
            CSV: 
            ground truth: 
            root: 
        '''
        
        frame = pd.read_csv('data/sample_cleansingWine100.csv')
        np_frame = frame.to_numpy()
        wine_same_class = []
        wine_other_class = []
        for wine in np_frame:
            same_class = []
            other_class = []
            for wine_other in np_frame:
                same_point = 0
                if wine[1] == wine_other[1]:
                    same_point+=1
                if wine[2] == wine_other[2]:
                    same_point+=1
                if wine[3] == wine_other[3]:
                    same_point+=1
                if wine[4] == wine_other[4]:
                    same_point+=1
                if wine[5] == wine_other[5]:
                    same_point+=1
                
                if same_point > 2:
                    same_class.append(wine_other)
                else:
                    other_class.append(wine_other)
            
            wine_same_class.append(same_class)
            wine_other_class.append(other_class)
            
        self.datasets = []
        for i in range(len(np_frame)):
            main_wine = np_frame[i]
            same_class = wine_same_class[i]
            other_class = wine_other_class[i]
            for same in same_class:
                for other in other_class:
                    data = []
                    data.append(main_wine)
                    data.append(same)
                    data.append(other)
                    self.datasets.append(data)

    def __len__(self):  #
        return len(self.datasets)

    def __getitem__(self, index):
        data = self.datasets[index]
        main_wine = data[0]
        same_wine = data[1]
        other_wine = data[2]
        
        main_wine_vector = self.normalize_encoding(main_wine)
        same_wine_vector = self.normalize_encoding(same_wine)
        other_wine_vector = self.normalize_encoding(other_wine)
        
        return main_wine_vector, same_wine_vector, other_wine_vector

    def one_hot_encoding(self, wine):
        '''
        len 22 vector
        5 + 5 + 5 + 5 + 5
        '''
        wine_vector = torch.zeros((5 * 5))
        for i, value in enumerate(wine[1:]):
            # print(i, value)
            # print(i*5 + (int(value)-1))
            wine_vector[i*5 + (int(value)-1)] = 1
            
        return wine_vector

    def normalize_encoding(self, wine):
        '''
        '''
        wine_vector = torch.tensor(wine[1:])
        wine_vector = (wine_vector-3) / 2
        return wine_vector.float()

# ---------------------------------------------------------------init-------------------------

def build_train_loader(cfg):

    train_data = WineDataSet()

    if dist.is_initialized():  # ?
        from torch.utils.data.distributed import DistributedSampler
        sampler = DistributedSampler(train_data)

    else:
        sampler = None

    data_loader = torch.utils.data.DataLoader(train_data,
                                              num_workers=4,
                                              batch_size=cfg.TRAIN.BATCH_SIZE,
                                              shuffle=True,
                                              pin_memory=True,
                                              drop_last=True,
                                              sampler=sampler)

    return data_loader


def build_val_loader(cfg):
    
    val_data = WineDataSet()
    if torch.distributed.is_available():
        from torch.utils.data.distributed import DistributedSampler
        sampler = DistributedSampler(val_data)
    else:
        sampler = None

    data_loader = torch.utils.data.DataLoader(val_data,
                                              num_workers=4,
                                              batch_size=1,
                                              shuffle=True,
                                              pin_memory=True,
                                              sampler=sampler)

    return data_loader