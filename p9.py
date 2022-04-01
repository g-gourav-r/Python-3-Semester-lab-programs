from tkinter import *
import random

window=Tk()
window.title("Program 9")
window.geometry("500x200")
message=StringVar()

lab1=Label(window,text="Random Program Assigner")
lab1.grid(row=0,column=1)
lab2=Label(window,text="Enter the number of Students")
lab2.grid(row=1,column=0)
students=Entry(window,width=40)
students.grid(row=1,column=1,pady=10)
lab3=Label(window,text="Enter the number of programs")
lab3.grid(row=2,column=0)
programs=Entry(window,width=40)
programs.grid(row=2,column=1,pady=10)
lab4=Label(window,textvariable=message)
lab4.grid(row=4)


def randass():
    studentno=students.get()
    programno=programs.get()
    detail=""
    if studentno.isnumeric() and programno.isnumeric():
        for i in range(1,int(studentno)+1):
            detail+="Student"+str(i)+"- Program number "
            detail+=str(random.randint(1,int(programno)))+"\n"
        file=open("students.csv",'w')
        file.write(detail)
        file.close()
        message.set("Done")
    else:
        message.set("Invalid")

assign=Button(window,text="Assign",command=randass)
assign.grid(row=3,column=1)
        
window.mainloop()
