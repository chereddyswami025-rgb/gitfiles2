import random

randnum=random.randint(1,10)
# print(randnum)
for i in range(1,5):
    gnum=int(input("enter guess number::"))
    if randnum==gnum:
        print("gnum is equal to randnum")
    elif randnum>gnum:
        print("guess num is lower than randnum")
    else:
        print("guess num is greater than randnum")
