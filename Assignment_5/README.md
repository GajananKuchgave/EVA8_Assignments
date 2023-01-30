# The 5th Assignment is about Batch Normalization + Regularization:

  ## Problem Statement
  You are making 3 versions of your 4th assignment's best model (or pick one from best assignments):
  
  1. Network with Group Normalization
      
  2. Network with Layer Normalization
      
  3. Network with L1 + BN
  ### You MUST:
  
  1. Write a single model.py file that includes GN/LN/BN and takes an argument to decide which normalization to include
    
  2. Write a single notebook file to run all the 3 models above for 20 epochs each
  
  ### Create these graphs:
  
  Graph 1: Test/Validation Loss for all 3 models together
    
  Graph 2: Test/Validation Accuracy for 3 models together
  
  graphs must have proper annotation
  
  Find 10 misclassified images for each of the 3 models, and show them as a 5x2 image matrix in 3 separately annotated images. 
  
  ### write an explanatory README file that explains:
  
  1. what is your code all about,
    
  2.  how to perform the 3 normalizations techniques that we covered(cannot use values from the excel sheet shared)
    
  3.  your findings for normalization techniques,
    
  4.  add all your graphs
    
  5. your 3 collection-of-misclassified-images 
    
  6. Upload your complete assignment on GitHub and share the link on LMS
    
 # Detailed Solution
 
  The purpose of the assignement is to understand the impact of the different Normalization techniques in the accuracy and loss error over the network.
  
  There are normalization techniques and their effects have been demonstrated as below 
  
  1. Network with L1 + BN
      
  2. Network with Group Normalization
      
  3. Network with Layer Normalization

![image](https://user-images.githubusercontent.com/46486710/215538451-06737281-5a0e-4be2-8b70-4612f458adad.png)


Batch Normalization: standardizes the inputs to a layer for each mini-batch of images

Group Normalization: Groups the channels over each image into multiple groups

Layer Normalization: Over all channel for each image.

# Graphs for accuracy and Loss for Training and Testing 

![image](https://user-images.githubusercontent.com/46486710/215540167-5f287749-9d04-4121-85d2-a51acf3c7c39.png)

![image](https://user-images.githubusercontent.com/46486710/215540408-449c67c4-d896-4bb2-acf1-774088e51275.png)


# 10 Misclassified images for Each Layer

1. batch Normalization + L1 Regularization

![image](https://user-images.githubusercontent.com/46486710/215541230-46c1e4f7-3a78-4920-b558-f15af6c8f4a6.png)

2. Group Normalization

![image](https://user-images.githubusercontent.com/46486710/215541390-0d34d89b-b5f2-40e8-9b10-2ed0d1b3c7d7.png)

3. Layer Normalization

![image](https://user-images.githubusercontent.com/46486710/215541555-bcc16747-f2ce-4df7-bac2-fd361055605c.png)




      
