import random
n=int(input("enter any number"))

r=random.randint(1,10)
print(r)
if n==r:
    print("you won game")
else:
    print("you lost game")