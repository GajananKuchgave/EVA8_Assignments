import torch.nn.functional as F
import torch.nn as nn
dropout_value = 0.1
num_groups = 4

def NormalizationFunction(method, out_channels):
  if(method == 'BN'):
    return nn.BatchNorm2d(out_channels)
  elif(method == 'LN'):
    return nn.GroupNorm(1, out_channels)
  elif(method == 'GN'):
    return nn.GroupNorm(num_groups, out_channels)

class Net(nn.Module):
    def __init__(self, normalizationMethod='BN'):
        super(Net, self).__init__()
        # Input Block
        self.convblock1 = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=32, kernel_size=(3, 3), padding=1, bias=False),
            nn.ReLU(),
            NormalizationFunction(normalizationMethod, 32),
            nn.Dropout(dropout_value),# output_size = 32  RF = 3
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=(3, 3), padding=0, bias=False),
            nn.ReLU(),
            NormalizationFunction(normalizationMethod, 32),
            nn.Dropout(dropout_value),# output_size = 30 RF = 5
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=(3, 3), padding=0, bias=False),
            nn.ReLU(),
            NormalizationFunction(normalizationMethod, 32),
            nn.Dropout(dropout_value)# output_size = 28 RF = 7
        ) 

        # CONVOLUTION BLOCK 1
        self.convblock2 = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=(3, 3), padding=1, bias=False),
            nn.ReLU(),
            NormalizationFunction(normalizationMethod, 32),
            nn.Dropout(dropout_value),# output_size = 28    RF = 9
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(3, 3), stride = 2, padding=0, bias=False),
            nn.ReLU(),
            NormalizationFunction(normalizationMethod, 64),
            nn.Dropout(dropout_value)
        ) # output_size = 14    RF = 18

        # TRANSITION BLOCK 1
        self.convblock3 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=32, kernel_size=(1, 1), padding=0, bias=False)
        ) # output_size = 12
        #self.pool1 = nn.MaxPool2d(2, 2) # output_size = 12 RF = 20

        # CONVOLUTION BLOCK 2
        self.convblock4 = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=(3, 3), padding=1, bias=False),
            nn.ReLU(),            
            NormalizationFunction(normalizationMethod, 32),
            nn.Dropout(dropout_value),# output_size = 12 RF = 22
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=(3, 3), stride = 2,padding=0, bias=False),
            nn.ReLU(),            
            NormalizationFunction(normalizationMethod, 32),
            nn.Dropout(dropout_value),# output_size = 12 RF = 22
            nn.Conv2d(in_channels=32, out_channels=10, kernel_size=(3, 3),padding=0, bias=False),
            nn.ReLU(),            
            NormalizationFunction(normalizationMethod, 10),
            nn.Dropout(dropout_value)
        ) # output_size = 4 RF = 46
        #self.convblock5 = nn.Sequential(
        #    nn.Conv2d(in_channels=16, out_channels=16, kernel_size=(3, 3), padding=0, bias=False),
        #    nn.ReLU(),            
        #    NormalizationFunction(normalizationMethod, 16),
        #    nn.Dropout(dropout_value)
        #) # output_size = 8
        #self.convblock6 = nn.Sequential(
        #    nn.Conv2d(in_channels=16, out_channels=16, kernel_size=(3, 3), padding=0, bias=False),
        #    nn.ReLU(),            
        #    NormalizationFunction(normalizationMethod, 16),
        #    nn.Dropout(dropout_value)
        #) # output_size = 6
        #self.convblock7 = nn.Sequential(
        #    nn.Conv2d(in_channels=16, out_channels=16, kernel_size=(3, 3), padding=0, bias=False),
        #    nn.ReLU(),            
        #    NormalizationFunction(normalizationMethod, 16),
        #    nn.Dropout(dropout_value)
        #) # output_size = 4
        
        # OUTPUT BLOCK
        self.gap = nn.Sequential(
            nn.AvgPool2d(kernel_size=4)
        ) # output_size = 1

        #self.convblock8 = nn.Sequential(
        #    nn.Conv2d(in_channels=64, out_channels=10, kernel_size=(1, 1), padding=0, bias=False)
        #) 

        #self.dropout = nn.Dropout(dropout_value)

    def forward(self, x):
        x = self.convblock1(x)
        x = self.convblock2(x)
        x = self.convblock3(x)
        x = self.convblock4(x)
        #x = self.convblock5(x)
        #x = self.convblock6(x)
        #x = self.convblock7(x)
        #x = self.fc2(F.relu(self.fc1(x))) 
        #x = self.fc1(x)
        x = self.gap(x)        
        #x = self.convblock8(x)
        #x = self.fc2(F.relu(self.fc1(x))) 

        x = x.view(-1, 10)
        return F.log_softmax(x, dim=-1)
