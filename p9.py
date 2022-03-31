from tkinter import *
import random

window = tkinter.Tk()
window.title("Program 9")
window.geometry("300x400")
msg=StringVar()

lab1=Label(window,text="Random program number assigner ")
lab1.grid(row=0)
lab2=Label(window,text="Enter the number of students")
lab2.grid(row=1,column=0)
students=Entry(window,width=25)
students.grid(row=1,column=1)
lab3=Label(window,text="Enter the number of programs")
lab3.grid(row=1,column=2)
programs=Entry(window,width=25)