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
    
 loss=0.32161745429039 batch_id=468: 100%|██████████| 469/469 [00:29<00:00, 15.93it/s]
<torch.utils.data.dataloader.DataLoader object at 0x7f69288a3e20> set: Average loss: 0.321, MNIST Accuracy:86.83, Addition_Accuracy:9.0

loss=0.3808058202266693 batch_id=468: 100%|██████████| 469/469 [00:29<00:00, 15.93it/s]
<torch.utils.data.dataloader.DataLoader object at 0x7f69288a3e20> set: Average loss: 0.302, MNIST Accuracy:87.39, Addition_Accuracy:9.09

loss=0.4174554646015167 batch_id=468: 100%|██████████| 469/469 [00:29<00:00, 15.96it/s]
<torch.utils.data.dataloader.DataLoader object at 0x7f69288a3e20> set: Average loss: 0.296, MNIST Accuracy:87.62, Addition_Accuracy:8.7

loss=0.20930629968643188 batch_id=468: 100%|██████████| 469/469 [00:29<00:00, 16.06it/s]
<torch.utils.data.dataloader.DataLoader object at 0x7f69288a3e20> set: Average loss: 0.289, MNIST Accuracy:87.76, Addition_Accuracy:8.36
