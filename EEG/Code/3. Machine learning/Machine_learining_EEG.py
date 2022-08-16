#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans, SpectralClustering
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_samples, silhouette_score

# In[56]:


data=pd.read_csv("Data_medians.csv")


# In[57]:


del data['Unnamed: 0']


# In[58]:


# 0: Awake
# 1: N1
# 2: N2
# 3: N3
# 4: REM

for i in range(0,len(data)):
    if data.iloc[i,35]=='Awake':
        data.iloc[i,35]=0
    elif data.iloc[i,35]=='N1':
        data.iloc[i,35]=1
    elif data.iloc[i,35]=='N2':
        data.iloc[i,35]=2
    elif data.iloc[i,35]=='N3':
        data.iloc[i,35]=3
    elif data.iloc[i,35]=='REM':
        data.iloc[i,35]=4
    else:
        data.iloc[i,35]=np.nan


# In[70]:


data_2=data.dropna()


# In[73]:


data_2.iloc[48]


# In[78]:


# Standardize the data
X = StandardScaler().fit_transform(data_2.iloc[:,:35])


# In[81]:


Y=data_2.iloc[:,35].to_numpy()


# In[111]:


X_train=X[:int(len(X)*0.9)]
X_test=X[int(len(X)*0.9):]


# In[112]:


Y_train=Y[:int(len(X)*0.9)]
Y_validate=Y[int(len(X)*0.9):]


# In[89]:


# Run local implementation of kmeans
model = KMeans(n_clusters=5, max_iter=100, init='random',n_init=10)


# In[90]:


model.fit(X_train)


# In[91]:


#Obtaining clusters centroid
centroids = model.cluster_centers_

#To obtain the labels of each cluster
labels = model.labels_


# In[96]:


matrix=np.zeros([6,6])
for i in range(0,len(labels)):
    matrix[labels[i],Y_train[i]]+=1
    matrix[5,Y_train[i]]+=1
    matrix[labels[i],5]+=1


# In[97]:


matrix


# In[104]:


from keras.models import Sequential
from keras.layers import Input, Dense, Flatten, Dropout
from keras.layers import Activation
from keras.optimizers import SGD
from keras.models import Model
from keras.utils import plot_model
from keras import initializers
from keras import optimizers
import tensorflow as tf


# In[106]:


#We define the numer of neurons in each layer. We cant change the numer of input or output neurons scince they correspond to the variables we already have.
n_x=35
n_h1=35
n_h2=15
n_y=5


# In[107]:


#Now we define the functions of each layer
model = Sequential()

input_nodes = n_x     #input layer has n_x nodes
hlayer1_nodes = n_h1   #first hidden layer has n_h1 nodes
hlayer2_nodes = n_h2   #second hidden layer has n_h2 nodes
output_nodes = n_y    #output layer has n_y node


#For the first hidden layer, it is necessary to indicate its input layer, which corresponds to 
#the input layer of the network

model.add(Dense(hlayer1_nodes,  kernel_initializer='identity', bias_initializer='zeros', input_dim=input_nodes, activation='tanh'))

model.add(Dense(hlayer2_nodes,  kernel_initializer='identity', bias_initializer='zeros', input_dim=n_h1, activation='tanh'))

#For any other hidden layer its input layer is not indicated. Its input layer is the hidden layer before it

#The following layer is the last layer of the network. It corresponds to the output layer of the network
model.add(Dense(output_nodes,activation='sigmoid'))


# In[129]:


train_y=Y_train.astype('float64')


# In[130]:


train_y=Y_train.reshape([141,1])


# In[132]:


Y_train=np.zeros([len(train_y),5])
for i in range(0,len(Y_train)):
    Y_train[i,int(train_y[i])]=1.


# In[125]:


# We define the optimizing function and their hyperparameters: learining rate(lr) in the present case
model.compile(loss='categorical_crossentropy', optimizer=optimizers.SGD(learning_rate=0.001), metrics=['accuracy'])


# In[133]:


validation_portion = 0.11
epochs = 500

#The network is trained 
history = model.fit(X_train, Y_train, epochs=epochs, validation_split = validation_portion)


# In[134]:


Y_train


# In[136]:


train_y


# In[ ]:




