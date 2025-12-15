
sum=0
for i in range(1,6):
    print(f"enter subject {i} marks::")#this is formatted output
    m=int(input("enter marks"))
    sum+=m
print(f"sum of total marks={sum}")
perc=(sum/500)*100
print(f"your marks percentage is {perc}")
