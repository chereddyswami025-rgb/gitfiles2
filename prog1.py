f=open("file1.txt","r+")
f.truncate(0)
f.write("python programming language")
f=open("file1.txt","r+")
c=f.read()
print(c)
d="".join(reversed(c))
print(d)
print(len(c))
for i in c:
    if i=="m":
        break
    print(i)
j=-26
tw=0
for j in c:
    if j==" ":
        tw+=1
print("total words=",tw+1)
f=open("file1.txt","w+")
f.append("\n  java programming language")
rd=f.read()
print(rd)