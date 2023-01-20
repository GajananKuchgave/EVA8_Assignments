# BackPropogation understanding using Excel
The Assignment is all about the understanding the BackPropoation by doing the calculations which help to adjust the weights and reduce the error.
Below image shown has 2 inputs, 2 hidden neurons and two output neurons used.
# Neural Network

![NN_Architecture](https://user-images.githubusercontent.com/46486710/213661275-09246acd-8334-4fa6-8759-d34b4c2a7e00.png)

    Initial input weights
      w1 = 0.15   w2 = 0.2   w3 = 0.25    w4 = 0.3
      w5 = 0.4    w6 = 0.45  w7 = 0.5     w8 = 0.55

# Forward Propogation Calculations
      At first layer, inputs are being multiplied with initial weights and to calculate h1 and h2
      h1 = i1*w1 + i2*w2 
      h2 = i1*w3 + i2*w4
  
The h1 and h2 has been passed to sigmoid activation layer to get the non linearity to the neural network
 
       a_h1 = σ(h1) = 1/(1+ exp(-h1))
       a_h2 = σ(h12) = 1/(1+ exp(-h2))
 
 We have another layer where we need to pass the output of last layer with the initial weights in that layer
 
       o1 = w5*a_h1 + w6*a_h2
       o2 = w7*a_h1 + w8*a_h2
 + We apply activation layer to the o1 and o2 
 
       a_o1 = σ(o1) = 1/(1+ exp(-o1))
       a_o2 = σ(o2) = 1/(1+ exp(-o2))
 
    + As we know the ouput values and what we have predicted the a_o1 and a_o2 as a output. So We need to calculate the error E1 and E2
 
 # Error Calculation(Loss)
 
    * E1 = 0.5 * (t1 - a_o1)^2
    * E2 = 0.5 * (t2 - a_o2)^2
    * E_Total = E1 +E2
 
 # Back Propogation
 
  back propogation is used for adjusting the weights and reducing the error loss to improve the accuracy
 
  Weight w5, w6 ,w7 and w8 adjusted with the below formulas
  
        δE_Total/δw5	=	δ( E1+E2)/δw5)			
        δE_Total/δw5	=	δE1/δw5		# removin E2 as there is no impact of E2 w.r.t w5	
        δE_Total/δw5	=	(δE1/δa_o1)*(δa_o1/δo1)*(δo1/δw5)			
        δE1/δa_o1	=	δ(0.5∗(t1 - a_o1)^2)/δa_o1 = (ao1 - t1)			
        δa_o1/δo1	=	δ(σo1)/δo1 = a_o1*(1-a_o1)			
        δo1/δw5	=	a_h1			

Calculate the partial derivative of E_Total w.r.t w5,w6,w7 and w8 as given below

      E_Total/δw5	=	(a_o1 - t1)*a_o1*(1 - a_o1)*a_h1			
      E_Total/δw6	=	 (a_o1 - t1)*a_o1*(1 - a_o1)*a_h2			
      E_Total/δw7	=	(a_o2 - t2)*a_o2*(1 - a_o2)*a_h1			
      E_Total/δw8	=	(a_o2 - t2)*a_o2*(1 - a_o2)*a_h2			

 Perform the Back Propgation through hidden layers
     
     δE1/δa_h1		   = (ao1 - t1)*a_o1*(1 - ao1)*w5					
     δE2/δa_h1		   = (ao2 - t2)*a_o2*(1 - ao2)*w7							
     δE_Total/δa_h1	 = (ao1 - t1)*a_o1*(1 - ao1)*w5 +(a_o2 - t2)*a_o2*(1 - ao2)*w7		
     
  Finally calculate the partial derivative of weights w1, w2, w3 and w4 w.r.t E_Total
  
      δE_Total/δw1	=	δE_Total/δa_h1*δa_h1/δh1*δh1/w1			
      δE_Total/δw2	=	δE_Total/δa_h1*δa_h1/δh1*δh1/w2			
      δE_Total/δw3	=	δE_Total/δa_h2*δa_h2/δh2*δh2/w3			
      δE_Total/δw4	=	δE_Total/δa_h2*δa_h2/δh2*δh2/w4			

  Now update all the weights by using the earlier weight minus learning rate(LR)* error
  
      w1 = w1 - LR * δE_Total/δw1
      w2 = w2 - LR * δE_Total/δw2
      w3 = w3 - LR * δE_Total/δw3
      w4 = w4 - LR * δE_Total/δw4
      w5 = w5 - LR * δE_Total/δw5
      w6 = w6 - LR * δE_Total/δw6
      w7 = w7 - LR * δE_Total/δw7
      w8 = w8 - LR * δE_Total/δw8
      
  # Error Graph w.r.t Different Learning rates
  
 We have used learning rates 0.1,0.2, 0.3, 0.5, 1.0 and 2.0. The graph shows that the more the learning rate, faster the error reduction.
 
 But optimal Learning rate need to be used to balance the accuracy and avoid the under fitting or over fitting effect
    
![Graph](https://user-images.githubusercontent.com/46486710/213683963-a6d2a978-6546-4da2-a2e6-81758b016a28.png)



					

 
 
  

  
 
