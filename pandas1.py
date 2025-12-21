import pandas as pd
import numpy as np
s=pd.Series([1,np.nan,6,7,5])# series is a single dimension array
# print(s)
# print(s.describe())
# print(s.max())
# print(s.min())
# print(s.mean())
# print(s.std())
p=s.map(lambda x:x**2)
# print(p.sort_values())
#if inplace=true it drops the particuar index and that affects into the original series,otherwise it doesn't affect
# drp=s.drop(3,inplace=False)#here 3 is index
# print(drp)
# print(s.isnull())
# print(s.notnull())
# s.fillna(30,inplace=True)
# print(s)
# print(p)
# dropped=s.dropna()
# print(dropped)
# print(s.iloc[2])
a=pd.Series([5,46,27,13,19],index=['a','b','c','d','e'])
print(a)