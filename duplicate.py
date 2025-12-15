l=['a',1,2,3,'b',2,'a']
print(l)
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            l.pop(j)
print(l)