#!/usr/bin/env python
# coding: utf-8

# In[9]:



#implementation of xor through neurons
import numpy as np
def calculate_layer1(x,w):
    #reshape x 
    x=x.reshape(1,3)
    #find the transpose of w
    w1=np.transpose(w)
    # find the net
    layer1=np.dot(x,w1)
    #use bipolar discrete activation function
    layer1[layer1>0]=1
    layer1[layer1<=0]=-1
    print(layer1)
    return layer1

def calculate_layer2(out,w):
    #append 1 to the output of layer1
    aug_out=np.append(out,[1])
    layer2 = calculate_layer1(aug_out,w)
    return layer2
x=np.array([[0,0,-1],[0,1,-1],[1,0,-1],[1,1,-1],])
w1=np.array([[-2,1,1/2],[1,-1,1/2],])
w2=np.array([[1,1,1],])


# In[ ]:





# In[ ]:





# In[ ]:




