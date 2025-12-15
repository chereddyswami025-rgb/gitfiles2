import numpy as np 
# arr1= np.array([1,2,3,4])
# print(np.max(arr1))
# print(np.min(arr1))
# print(np.mean(arr1))

# print(np.full([3,3],7))
# arr2=np.arange(1,13)
# arr3=arr

# print(np.arange(1,5).reshape(2,2)+np.arange(6,10).reshape(2,2))

arr6=np.arange(1,5).reshape(2,2)
arr7=np.arange(6,10).reshape(2,2)
# print(np.multiply(arr6,arr7))

# print(arr7)
# print(np.max(arr7))
# print(arr7.T)

# arr8=np.arange(5,11)>8
# print(arr8)

arr9=np.arange(1,25).reshape(2,3,4)
print(arr9)
print(np.swapaxes(arr9,1,2))#it  swaps the axes of array 1=3,2=4
# print(arr9)
# print(arr9.T)