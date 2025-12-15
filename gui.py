import tkinter
from tkinter import *
from tkinter import ttk


from tkinter import messagebox
root=tkinter.Tk()#here Tk is a class
root.title("demo")
root.geometry("600x600")
 # label=Label(root,text="header").pack()
# btn=Button(root,text="buton1",bg="blue").pack(side=RIGHT)#add widgets at right side of the webpage
# btn.grid(column=2,row=3)
#radio
# rb=Radiobutton(root,text="python",value=1).pack()
# rb1=Radiobutton(root,text="java",value=2).pack()
# rb1=Radiobutton(root,text="c++",value=3).pack()
# e=Entry(root,width=20).pack()

# def mfun():
#     messagebox.showinfo("status","tkinter used for guii in python").pack()

# mb=Button(root,text="python",command=mfun).pack()#pack add widgets to the webpage

#combobox
n=tkinter.StringVar()
def greet():
    n.set("hello everyone")

lab1=Label(root,text="chaduvukondi firstu",textvariable=n).place(x=100,y=100)
tbtn=Button(root,text="str",command=greet).place(x=40,y=100)

root.mainloop()