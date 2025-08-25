import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
#
data = pd.read_csv('content.csv')
print(data.head())

#extrating data from dataset 
x = data.iloc[:,2:].values
# Convert to numeric, replacing non-numeric values with 0
x = pd.DataFrame(x).apply(pd.to_numeric, errors='coerce').fillna(0).values

#reshaping the extracted data into a reasonable size
x = x[0].reshape(int(np.sqrt(len(x[0]))), -1).astype('uint8')  # Use first row and calculate square dimensions
plt.imshow(x, cmap='gray')
plt.show()
print(x)