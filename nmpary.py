import numpy as np

#it creates array with the spcified range of numbers
# a=np.arange(1,6) 
# print(a)

# #1d array
# a1=np.array([1,2,5,4,3,6,3,4,9])
# print(a1)

# a2=np.array([[1,2,3,4,5],
#            [6,7,8,9,0]])
# print(a2)

#np.zeros() by default creates an array filled with 0.0(float numbers)
# a3=np.zeros([2,3,4])# here 2,3,4 is a dimensions
# print(a3.dtype)

# #np.ones() by default creates an array filled with 1.0(float numbers)
# a4=np.ones([2,3,4,5],dtype=int)
# print(a4.dtype)

# b3=np.arange(1,49).reshape(2,3,4,2)
# print(b3)

# b4=np.full([2,3,4],5) #it gives array filled with 5 according to specific dimensions  
# print(b4)

# arr_sum=np.add([[1,2,3],[4,5,6]],[[3,4,5],[6,7,8]])
# print("arr=",arr_sum)

# arr_sub=np.subtract([3,4,5,6],[7,8,9,10])
# print("arr=",arr_sub)

# arr_mul=np.multiply([1,2,3],[5,6,7])
# print(arr_mul)

# arr_div=np.divide([1,2,3],[4,5,6])
# print(arr_div)



# arr_pow=np.power([1,2,3],[4,5,6])
# print(arr_pow)


# arr_mod=np.mod([1,2,3],[4,5,6])
# print(arr_mod)

# ar1=np.arange(2,6)
# ar2=np.arange(2,6)
# arr_po=np.power(ar1,ar2)
# print(arr_po)

#np.multiply is not same as matrix multiplication
# arr_mul=np.multiply([[1,2],[4,5]],[[2,3],[5,6]])
# print(arr_mul)

#it is a matrix multiplicatio;n
# arr1=np.array([[1,2],
#                [4,5]])
# arr2=np.array([[2,3],
#                [4,6]])
# print(arr1@arr2)
# print(np.dot(arr1,arr2))


# a=np.array([1,2,3,4,5])
# b=np.array([6,4,3,2,1])
# relational operations
# print('==',a==b)
# print("!=",a!=b)
# print(">",a>b)
# print("<",a<b)
# print(">=",a>=b)
# print("<=",a<=b)

#indexing for 1d arrays
# print("last element:",a[-1])
# print("first element:",a[0])

#slicing for 1d arrays
# print(a[:3])
# print(a[::-1])
# print(b[1:4])

#indexing for 2d arrays
# print(arr2[1,0])
# print(arr1[-1,-2])
# print(arr1[0,1])

#slicing for 2d arrays
# ary1=np.array([[1,2,3,4],
#                [5,6,7,8],
#                [3,4,5,6]])

# print(ary1[0:2,1:3])#selects rows 0,1 and columns 1,2

#modify slice
# ary1[0:2,1:3]=([33,44],[44,55])
# print(ary1)

#negative indexing
# print(ary1[-1,-3])
# print(ary1[-2,2])

#boolean indexing
# myarr1=np.array([3,4,5,6,8,9,12,11,14])
# upd_arr=myarr1>5

# print(upd_arr)
# print(myarr1[upd_arr])#displays elements which satisfy only condition

# res_arr=ary1>4
# print(res_arr)
# print(ary1[res_arr])

#fancing indexing
# indices=[2,4,1,6]
# print(myarr1[indices])

#transposing matrix
# new_arr=ary1.T
# print(new_arr)

# t_arr=np.array([[[1,2,3],
#                 [4,5,6],
#                 [7,8,9]],
#                 [[10,11,12],
#                 [13,14,15],
#                 [16,17,18]]])
# swap_arry=np.swapaxes(t_arr,0,2)

# print(swap_arry) 

#pseudo random number generation
# random_arr=np.random.randint(1,100,size=5)
# print(random_arr)


#matrix multiplication
# m1=np.array([[1,2,3],
#              [5,6,7]])
# m2=np.array([[8,5],
#             [4,3],
#             [8,6]])
# m3=np.matmul(m1,m2)
# print(m3)

# x=np.arange(1,5)
# y=x.reshape(2,2)
# print(y)

#reshaping of random numbers array
# m4=np.random.randint(1,100,size=4)
# print(m4)
# m5=m4.reshape(2,2)#converts into matrix
# print(m5)

#aggregation functions

# m6=np.arange(1,10)
# print(m6)
# m7=m6.reshape(3,3)
# print(m7)
# #aggregationn functions
# print("sum=",np.sum(m7))
# print("max=",np.max(m7))
# print("max=",np.min(m7))
# print("mean=",np.mean(m7))

#universal functions
# print("add=",np.add(m7,3)) 
# print("multiply=",np.multiply(m7,3))
