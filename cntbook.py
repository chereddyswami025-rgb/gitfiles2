class contact:
    count=0
    def addcnt(self):
        self.id=self.count+1
        self.name=input("enter name::")
        self.phone=int(input("enter contact::"))
        self.email=input("enter mail::")
        self.address=input("enter address::")
    
    def viewcnt(self):  
        print(f"id={self.id}")
        print(f"name={self.name}")
        print(f"phone={self.phone}")      
        print(f"email={self.email}")
        print(f"address={self.address}")
    def updatecnt(self):
        pass

cnl=[]
c1=contact()
c2=contact()
cnl.append(c1,c2)

i=1
while(i!=0):
    if n==1:
        addcnt()