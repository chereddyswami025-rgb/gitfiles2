import pandas as pd
import numpy as np

#we give null values in series like np.nan
s=pd.Series([1,np.nan,6,7,5])# series is a single dimension array
# print(s)

# print(s.describe())#describes the array
# print(s.max())
# print(s.min())
# print(s.mean())
# print(s.std())#calculates standard deviation

p=s.map(lambda x:x**2)
# print(p.sort_values())
#if inplace=true it drops the particuar index and that affects into the original series,otherwise it doesn't affect
# drp=s.drop(3,inplace=False)#here 3 is index
# print(drp)
# print(s.isnull())
# print(s.notnull())


#filling missed values
# s.fillna(30,inplace=True)
# print(s)
# print(p)


#dropping missed values
# dropped=s.dropna()
# print(dropped)

#indexing
# print(s)
# print(s.iloc[2])#iloc means integer location
# print(s.iloc[-1])

# print(s.loc[3])#location based indexing
# a=pd.Series([5,46,27,13,19],index=['a','b','c','d','e'])
# print(a)

#accessing using elements using iloc
# print(a.iloc[2])#we can only give integer index in iloc

# print(a)

#accessing using elements using loc
# print(a.loc['c'])#in loc we can give the index of array elements which we provide
# print(a.loc['b':'e'])#slicing

#filter it returns the numbers which are gerater than 19 in array "a"
# filter=a[a > 19]
# print(filter)

s.fillna(10,inplace=True)
# print(s)
# print(s.sum())
# print(s)
# print(s.cumsum())#cumsum adds current element with it's previous element in series


#performs more than one operation at a time
# aggregated=s.aggregate(['sum','mean','std'])#perform given operations on "s" array
# print(aggregated)

#dataframes in pandas
data = {
    "student_id": [101, 102, 103, 104, 105],
    "name": ["Anil", "Bhavya", "Charan", "Divya", "Eshan"],
    "age": [20, 21, 19, 22, 20],
    "course": ["Python", "Data Science", "Python", "AI", "Data Science"],
    "marks": [78, 85, 67, 90, 72]
}

df=pd.DataFrame(data)
#head displays first few records defaultly,if you give any parameter in head then it displays particular number of rows
print(df.head(2))

