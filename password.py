import random

letters="abcdefghijklmnopqrstuvwxyz0123456789"
p="".join(random.choices(letters,k=8))#k is used to get k no of random items
print(p)

#**random.choices() is used to select MULTIPLE random items from a sequence.    