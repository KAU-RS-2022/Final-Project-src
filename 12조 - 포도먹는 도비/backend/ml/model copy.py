
# import torchvision
# import torchvision.datasets as dset
# import torchvision.transforms as transforms
# from torch.utils.data import DataLoader,Dataset
import matplotlib.pyplot as plt
import torchvision.utils
import numpy as np
import random
from PIL import Image
import torch
# from torch.autograd import Variable
import PIL.ImageOps    
import torch.nn as nn
from torch import optim
import torch.nn.functional as F



class SiameseNetwork(nn.Module):
    def __init__(self):
        super(SiameseNetwork, self).__init__()

        self.fc1 = nn.Sequential(
            nn.Linear(25, 64),
            nn.Sigmoid(),
        
            

            nn.Linear(64, 256),
            nn.Sigmoid(),
            
            nn.Linear(256, 64),
            nn.Sigmoid(),

            nn.Linear(64, 25),
            # nn.Sigmoid(),
        )

    def forward_once(self, x):
        # output = self.cnn1(x)
        # output = output.view(output.size()[0], -1)
        output = self.fc1(x)
        return output

    def forward(self, input1, input2):
        output1 = self.forward_once(input1)
        output2 = self.forward_once(input2)
        
        res = self.L2(output1, output2)
        # output = 
        
        
        return res

    def L2(self, output1, output2):
        # print(output1 == output2)
        output= F.pairwise_distance(output1, output2, keepdim = True)
        # print('L2',output.shape)
        
        return output
        
    
class ContrastiveLoss(torch.nn.Module):
    """
    Contrastive loss function.
    Based on: http://yann.lecun.com/exdb/publis/pdf/hadsell-chopra-lecun-06.pdf
    """

    def __init__(self, margin=2.0):
        super(ContrastiveLoss, self).__init__()
        self.margin = margin

    def forward(self, output1, output2, label):
        euclidean_distance = F.pairwise_distance(output1, output2, keepdim = True)
        loss_contrastive = torch.mean((1-label) * torch.pow(euclidean_distance, 2) +
                                      (label) * torch.pow(torch.clamp(self.margin - euclidean_distance, min=0.0), 2))


        return loss_contrastive
    
if __name__ == '__main__':
    model = SiameseNetwork()
    input= torch.ones([64,25])
    output = model(input)
    print(output.shape)