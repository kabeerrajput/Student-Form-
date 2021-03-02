from tkinter import *
root=Tk()
root.title("Student Form")

l=Label(text="Student Form",width=50,font=("bold",20)).pack()   
l_name = Label(root, text = "Enter Details").pack()

name=Label(root,text="Name",font=("bold",15)).pack()
name=Entry(root)
name.pack()

f_name=Label(root,text="Father Name",font=("bold",15)).pack()
f_name=Entry(root)
f_name.pack()

age=Label(root,text="Age",font=("bold",15)).pack()
age=Entry(root)
age.pack()

Class=Label(root,text="Class",font=("bold",15)).pack()
Class=Entry(root)
Class.pack()

var1 = IntVar()
var2 = IntVar()

def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        return"Python"
    elif (var1.get() == 0) & (var2.get() == 1):
        return"C++"
    elif (var1.get() == 0) & (var2.get() == 0):
        return"none"
    else:
        return"Python , C++"

r=StringVar()
r.set("female")

def clicked(value):
    
   myLabel=Label(root,text=r.get())
   myLabel.pack() 
   name1=name.get()
   s= name1.capitalize()
   print(s) 

   father=f_name.get()  
   print(father)
   
   age1=age.get()
   print(age)
   
   Class1=Class.get()
   print(Class)
   
   course=print_selection()
   
   l1=Label(root,text=name1).pack()
   l2=Label(root,text=father).pack()
   l3=Label(root,text=age1).pack()
   l4=Label(root,text=Class1).pack()
   
   l5=Label(root,text=course).pack()

gender=Label(root,text="Select Gender")
gender.pack()

Radiobutton(root,text="Male",variable=r,value="Male").pack()
Radiobutton(root,text="Female",variable=r,value="Female").pack()

course1=Label(root,text="Select Course")
course1.pack()

c1 = Checkbutton(root, text='Python',variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2 = Checkbutton(root, text='C++',variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()



def popup():
    response=messagebox.askyesno("Alert","Are you want to Registerd")
   
    Label(root,text=response).pack()
    if response==1:
        Label(root,text="You clickes Yes!").pack()
    else:
          Label(root,text="You clickes No!").pack()
btn=Button(root,text="Confirm",command=popup).pack()

def open():
    
    btn=Button(root,text="Submit",command=lambda:clicked(r.get())).pack()


root.mainloop()


