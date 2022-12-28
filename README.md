# EVA8_Assignments
The repository contains all the assignments from EVA8 Course on the Artificial Neural Networks
EVA8_MNIST_PyTorch dataset

The Neural Network takes 2 Inputs:
  an image from the MNIST dataset (say 5), and
  a random number between 0 and 9, (say 7)
  
  and gives two outputs:
    the "number" that was represented by the MNIST image (predict 5), and
    the "sum" of this number with the random number and the input image to the network (predict 5 + 7 = 12)
    
    #Training Log
    
 loss=1.0637370347976685 batch_id=468: 100%|██████████| 469/469 [00:28<00:00, 16.18it/s]
<torch.utils.data.dataloader.DataLoader object at 0x7f69288a3e20> set: Average loss: 1.022, MNIST Accuracy:65.18, Addition_Accuracy:7.79
loss=0.5416896343231201 batch_id=468: 100%|██████████| 469/469 [00:30<00:00, 15.45it/s]
<torch.utils.data.dataloader.DataLoader object at 0x7f69288a3e20> set: Average loss: 0.672, MNIST Accuracy:75.89, Addition_Accuracy:7.82
loss=0.4748753607273102 batch_id=468: 100%|██████████| 469/469 [00:29<00:00, 16.11it/s]
<torch.utils.data.dataloader.DataLoader object at 0x7f69288a3e20> set: Average loss: 0.372, MNIST Accuracy:86.4, Addition_Accuracy:9.09
loss=0.390163391828537 batch_id=468: 100%|██████████| 469/469 [00:29<00:00, 16.07it/s]
<torch.utils.data.dataloader.DataLoader object at 0x7f69288a3e20> set: Average loss: 0.312, MNIST Accuracy:88.08, Addition_Accuracy:8.85
