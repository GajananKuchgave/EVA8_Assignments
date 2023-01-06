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
    
 Training_loss=1.5795272588729858 batch_id=468: 100%|██████████| 469/469 
 Average loss: 0.013,   MNIST Accuracy:72.69,   Addition_Accuracy:8.13


Training_loss=1.2168940305709839 batch_id=468: 100%|██████████| 469/469 
Average loss: 0.010,   MNIST Accuracy:96.55,   Addition_Accuracy:9.76


Training_loss=1.1245989799499512 batch_id=468: 100%|██████████| 469/469 
Average loss: 0.009,   MNIST Accuracy:97.48,   Addition_Accuracy:10.09


Training_loss=1.0494039058685303 batch_id=468: 100%|██████████| 469/469 
Average loss: 0.008,   MNIST Accuracy:98.25,   Addition_Accuracy:10.17


Training_loss=0.9079716205596924 batch_id=468: 100%|██████████| 469/469 
Average loss: 0.007,   MNIST Accuracy:98.54,   Addition_Accuracy:10.28
