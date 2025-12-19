import numpy as np
import random as rd
arr1=np.arange(1,10)
# print(arr1.dtype)
def even(x):
    if x%2==0:
        return int(x)
    else:
        pass

# e_arr=list(map(even,arr1))#map function returns object so we have to convert into the list
# print(e_arr)

# #join works with only strings
# l1=["india","usa"]
# country="".join(l1)
# print(country)
# word=input("enter word::")
# name="".join(word)#joins the word into name
# print(name)


arr3=np.arange(8,15)
print(arr3)
# arr4=arr3>10
# print(arr3[arr4])
# arr3[arr4]=[0,0,0,0]
# print(arr3)
for i in range(-3,0):
    print(arr3[i])

arr4=arr3.astype(float)
print(arr4.dtype)