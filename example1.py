class sample1:
    def __init__(self):
        self.total=0
    def addf(self):
        self.total+=int(input("enter money"))

    def showbal(self):
        print("balance=",self.total)

    def subf(self):
        m=int(input("enter money you want"))
        self.total=self.total-m


s=sample1()

i=1
while i==1:
    ch=int(input("enter choice"))
    if ch==1:
        s.addf()
    elif ch==2:
        s.subf()
    else:
        s.showbal()
    i=int(input("enter 1 if you want to continue or 0 to stop "))

    


 