import numpy as np
import pandas as pd

#a list of first 20 numbers
ls = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(ls)
#printing the squares
b = [ls**2 for ls in range(1,21)]
print(b)

#Finding the middle value in a sorted list of number
L=[3,5,1,9]
L.sort()
print(L)
c=(L[2]+L[3])/2
print(c)
#using numpy
d=np.median(L)
dic={'name':'John','age':25}
print(dic)
data={
    'name':['Ian','Roy','Lebron'],
    'department':['IT','HR','Finance'],
    'funding':[100000,200000,300000],
    'location':['Mombasa','Nairobi','Kisumu']
}
pd.DataFrame(data)

