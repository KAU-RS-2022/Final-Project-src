
# import torchvision
# import torchvision.datasets as dset
# import torchvision.transforms as transforms
import torch
import torch.nn as nn
import torch.nn.functional as F



class SiameseNetwork(nn.Module):
    def __init__(self):
        super(SiameseNetwork, self).__init__()

        self.fc1 = nn.Sequential(
            nn.Linear(5, 32),
            nn.BatchNorm1d(32),
            nn.ReLU(inplace=True),

            nn.Linear(32, 32),
            nn.BatchNorm1d(32),
            nn.ReLU(inplace=True),
            
            nn.Linear(32, 16)
            # nn.Sigmoid(),
        )
        self.fc2 = nn.Sequential(
            nn.Linear(32, 32),
            nn.BatchNorm1d(32),
            nn.ReLU(inplace=True),
            nn.Linear(32, 32),
            nn.BatchNorm1d(32),
            nn.ReLU(inplace=True),
            nn.Linear(32, 1)
        )

    def forward_once(self, x):
        # output = self.cnn1(x)
        # output = output.view(output.size()[0], -1)
        output = self.fc1(x)
        return output

    def forward(self, input1, input2):
        output1 = self.forward_once(input1)
        output2 = self.forward_once(input2)
        
        # feats = torch.cat([output1, output2], dim=1)

        # output = self.fc2(feats)
        res = self.L2(output1, output2)
        res = 1/res
        output = torch.log(res)
        # output = 
        return output

    def L2(self, output1, output2):
        # print(output1 == output2)
        output= F.pairwise_distance(output1, output2, keepdim = True)
        # print('L2',output.shape)
        return output
        
    
    
if __name__ == '__main__':
    model = SiameseNetwork()
    input= torch.ones([64,25])
    output = model(input)
    print(output.shape)