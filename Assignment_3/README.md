
 # Training MNIST Dataset with Neural Network with less than 20k parameters and achieve greater than or equal to 99.40% accuracy
  
  The model has been trained with 16848 parameters.
  
  The model has been trained using BN, Dropout, a Fully connected layer, and GAP. 
  
  # Neural Network
  
    conv1 = Sequential(                     #input-28x28x1    #RF -3x3  #Output 26x26x16
            Conv2d(1, 16, 3, bias=False),
            ReLU(),          
            BatchNorm2d(16),  
            Dropout2d(0.25),
            Conv2d(16, 16, 3, bias=False),           #input-26x26x16   #RF -5x5  #Output 24x24x16      
            ReLU(), 
            BatchNorm2d(16),          
            Conv2d(16, 16, 3, bias=False),           #input-24x24x16   #RF -7x7  #Output 22x22x16
            ReLU(),         
            BatchNorm2d(16), 
            MaxPool2d(2, 2)                          #input-22x22x16   #RF -7x7  #Output 11x11x16
        )    

     conv2 = Sequential(                     #input-11x11x16   #RF -16x16  #Output 9x9x16
            Conv2d(16, 16, 3, bias=False),          
            ReLU(),          
            BatchNorm2d(16),   
            Dropout2d(0.25), 
            Conv2d(16, 16, 3, padding=1, bias=False),  #input-9x9x16   #RF -18x18  #Output 9x9x16   
            ReLU(),
            BatchNorm2d(16),
            Dropout2d(0.1),
            Conv2d(16, 16, 3,bias=False),             #input-9x9x16   #RF -20x20  #Output 7x7x16
            ReLU(),
            BatchNorm2d(16),
            Dropout2d(0.1),
            Conv2d(16,32, 3, bias=False),             #input-7x7x16   #RF -22x22  #Output 5x5x32
            ReLU(),
            BatchNorm2d(32),
            Dropout2d(0.25),        
        )

   conv_final = Conv2d(32, 10, 1, bias=False) #input-5x5x32 Output: 1x1x32 
   avgP = AvgPool2d(5)            
  
  
  # Below is the Training Log
  
  epoch  17
loss=0.05122385546565056 batch_id=468: 100%|██████████| 469/469 [00:15<00:00, 30.62it/s]

Test set: Average loss: 0.0194, Accuracy: 9941/10000 (99.41%)


epoch  18
loss=0.08080018311738968 batch_id=468: 100%|██████████| 469/469 [00:15<00:00, 30.63it/s]

Test set: Average loss: 0.0207, Accuracy: 9942/10000 (99.42%)


epoch  19
loss=0.01844112016260624 batch_id=468: 100%|██████████| 469/469 [00:15<00:00, 30.60it/s]

Test set: Average loss: 0.0183, Accuracy: 9948/10000 (99.48%)


epoch  20
loss=0.11876959353685379 batch_id=468: 100%|██████████| 469/469 [00:15<00:00, 30.83it/s]

Test set: Average loss: 0.0196, Accuracy: 9943/10000 (99.43%)

