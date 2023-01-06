# EVA8_Assignments
The repository contains all the assignments from EVA8 Course on the Artificial Neural Networks
EVA8_MNIST_PyTorch dataset

The Neural Network takes 2 Inputs:
  1. an image from the MNIST dataset (say 5)
  
  2. a random number between 0 and 9, (say 7)
  
  3. gives two outputs:
 
    a) the "number" that was represented by the MNIST image (predict 5)
    
    b) the "sum" of this number with the random number and the input image to the network (predict 5 + 7 = 12)
    
# Data Representation
  
1. Mixed the both MNIST data and Hot encoder Random number at the fully connected layer
2. used 19 parameters as a output for the prediction

# Training and Testing Log
    
 Training_loss=1.448 batch_id=468: 100%|██████████| 469/469 [00:25<00:00, 18.53it/s]
 
 set: Average loss: 0.012,   MNIST Accuracy:91.220,     Addition_Accuracy:9.920


Training_loss=1.245 batch_id=468: 100%|██████████| 469/469 [00:25<00:00, 18.28it/s]

 set: Average loss: 0.010,   MNIST Accuracy:96.360,   Addition_Accuracy:10.010


Training_loss=1.138 batch_id=468: 100%|██████████| 469/469 [00:25<00:00, 18.42it/s]

 set: Average loss: 0.009,   MNIST Accuracy:97.780,   Addition_Accuracy:9.620


Training_loss=1.038 batch_id=468: 100%|██████████| 469/469 [00:25<00:00, 18.56it/s]

 set: Average loss: 0.008,   MNIST Accuracy:98.490,   Addition_Accuracy:9.710
