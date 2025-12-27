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
    "name": ["Rahul", "Priya", "Aman", "Neha", "Vikas"],
    "age": [20, 21, 19, 22, 20],
    "course": ["Python", "Data Science", "Python", "AI", "Data Science"],
    "marks": [78, 85, 67, 90, 72]
}

df=pd.DataFrame(data)
#head displays first few records defaultly,if you specify any parameter in head then it displays specified number of rows
# print(df.head(3))



'''merge works on multiple dataframes
we must specify common column to merge
if a common column have different value then it can't be performs merge'''
data1={
    "id": [1, 2, 3, 4, 5],
    "name": ["Rahul", "Priya", "Aman", "Neha", "Vikas"],
    "age": [24, 28, 22, 35, 30],
    "city": ["Delhi", "Mumbai", "Chennai", "Hyderabad", "Pune"] 
    }   
    
df1=pd.DataFrame(data1)
# print(df1)

data2= {
    "name": ["Vikas","Aman", "Priya", "Neha","Rahl" ],
    "subject": ["Maths", "Science", "English", "Maths", "Science"],
    "marks": [85, 90, 78, 88, 92]
    }

df2=pd.DataFrame(data2)


''' you can assign many values to how
left:it displays all the records in left table and only matched from right table
right:it displays all the records in right table and only matched from left table
inner:it displays only matched records
outer:it displays all records from both tables'''

merge1=pd.merge(df1,df2,on='name',how="outer")
# print(merge1)

#if you want to merge more than two tables,merge like below
merge2=pd.merge(merge1,df,on='name')
# print(merge2)

imp_ds=pd.read_csv("top_1000_most_swapped_books.csv")
# print(imp_ds.head(10))
# print(imp_ds.tail(5))
# print(imp_ds.columns)

#it displays title,genre column of 98th row
# print(imp_ds.loc[98,['title','genre']])

#selecting range of rows and multiple columns by labels
# print(imp_ds.loc[10:20,['title','author','genre']])
m_cond=imp_ds.loc[(imp_ds['genre']=="fantasy") & (imp_ds['age_category']=="Adult")]
# print(m_cond)

#prints  single row we specified
# print(imp_ds.loc[10])

# print(imp_ds.head(15))

#it displays 12th index and 1,2,3,4 columns
# print(imp_ds.iloc[13,[1,2,3,4]])

#it displays 10 to 15 rows and 1,2 columns
# print(imp_ds.iloc[10:15,1:3])

#it displays values at index 1(row) and genre
# print(imp_ds.at[1,'genre'])

#prints title only of specified index
# x=imp_ds.loc[1,'title']
# print(x)
# y=imp_ds[(imp_ds['movie_release_year']>2015)&(imp_ds['age_category']=='Adult')]
# print(len(y))

# print(imp_ds.head(10))

# print(n_ds)

#axis=0 for droping rows and 1 for dropping columns
# n_ds=imp_ds.drop('author',axis=1)
# print(n_ds.head(5))

#if we want to drop entire row then give index and axis=0
# m=imp_ds.drop(3,axis=0)
# print(m.head(5))
'''updating values at specified index'''
# imp_ds.at[1,'author']='swami'
# print(imp_ds.head(10))
#print(imp_ds.describe())

#adding new column to the dataset temorarily if you give inplave=true then it will be permanent
# imp_ds['n_col']='default val'
print(imp_ds.head(5))

x=imp_ds.at([2,'title'])='rich dad poor dad'
print(imp_ds.head(5))
