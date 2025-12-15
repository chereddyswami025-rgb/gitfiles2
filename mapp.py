#map() is used to apply a function to every item in a list, tuple, or any iterable.
#map(function, iterable)
# function → what operation you want to apply
# iterable → list, tuple, string, etc.

l=[2,3,4,6,7]


res=map(str,l)#converts each item in a list into string
print(list(res))