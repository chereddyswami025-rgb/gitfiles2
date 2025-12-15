import tkinter
from tkinter import *

root=tkinter.Tk()
root.title("calc")
root.geometry("600x600")
 
num=IntVar()
def show(a):
  num.set(a)
   


btn=Button(root,text=1,command=lambda:show(1)).place(x=10,y=20)
btn1=Button(root,text=2,command=lambda:show(2)).place(x=50,y=20)

label1=Label(root,textvariable=num).place(x=40,y=30)
root.mainloop()