from tkinter import *
import random

window = Tk()
window.title("Program 9")
window.geometry("300x400")
errmsg=StringVar()

lab1=Label(window,text="Random program number assigner ")
lab1.grid(row=0)
lab2=Label(window,text="Enter the number of students")
lab2.grid(row=1,column=0)
students=Entry(window,width=25)
students.grid(row=1,column=1)
lab3=Label(window,text="Enter the number of programs")
lab3.grid(row=2,column=0)
programs=Entry(window,width=25)
programs.grid(row=2,column=1)

def randassign():
  studentNo=students.get()
  programNo=programs.get()
  detail=""
  if studentNo.isnumeric() and programNo.isnumeric():
    for s in range(1,int(studentNo)+1):
      detail+="student"+str(s)+ ", Program "+str(random.randint(1,programNo+1))+"\n"
      file=open("Studentprog.csv",'w')
      file.write(details)
      file.close()
      errmsg.set("Successfully assigned the values")
  else:
    errmsg.set("Not a valid input")
assign=Button(window,width=10,text="Assign",command=randassign)
assign.grid(row=3)
msg=Label(window,textvariable=errmsg)
msg.grid(row=4,column=0)

window.mainloop()
  