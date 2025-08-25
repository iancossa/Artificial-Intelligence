#%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


data = pd.read_csv('content.csv')
print(data.head())

#extrating data from dataset 
x = data.iloc[3,1:].values

#reshaping the extracted data into a reasonable size
#y = np.ravel(data.iloc[:,1:2].values)
x= x.reshape(28,28).astype('uint8')
plt.imshow(x, cmap='gray')
plt.show()
print(x)

#time to prepare the data,separate the labels and data values
df_y=data.iloc[:,1:]
df_z=data.iloc[:,0]

y_train,y_test,z_train,z_test=train_test_split(df_y,df_z,test_size=0.2,random_state=4)
print(y_train.head())#check data
print(z_train.head())#check data