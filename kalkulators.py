from distutils import command
from hashlib import new
import numbers
from sqlite3 import Row
from tkinter import*
from turtle import clear
mansLogs=Tk()
mansLogs.title("kalkulators")

e=Entry(mansLogs,width=15,font=("Arial Black",20))
btn0=Button(mansLogs, text=0, padx="40",pady=20,command=lambda:btnClick(0))
btn1=Button(mansLogs, text=1, padx="40",pady=20,command=lambda:btnClick(1))
btn2=Button(mansLogs, text=2, padx="40",pady=20,command=lambda:btnClick(2))
btn3=Button(mansLogs, text=3, padx="40",pady=20,command=lambda:btnClick(3))
btn4=Button(mansLogs, text=4, padx="40",pady=20,command=lambda:btnClick(4))
btn5=Button(mansLogs, text=5, padx="40",pady=20,command=lambda:btnClick(5))
btn6=Button(mansLogs, text=6, padx="40",pady=20,command=lambda:btnClick(6))
btn7=Button(mansLogs, text=7, padx="40",pady=20,command=lambda:btnClick(7))
btn8=Button(mansLogs, text=8, padx="40",pady=20,command=lambda:btnClick(8))
btn9=Button(mansLogs, text=9, padx="40",pady=20,command=lambda:btnClick(9))
btnP=Button(mansLogs, text="+", padx="40",pady=20,command=lambda:btnCommand("+"))
btnD=Button(mansLogs, text="/", padx="40",pady=20,command=lambda:btnCommand("/"))
btnC=Button(mansLogs, text="C", padx="40",pady=20,command=lambda:Clear())
btnR=Button(mansLogs, text="*", padx="40",pady=20,command=lambda:btnCommand("*"))
btnM=Button(mansLogs, text="-", padx="40",pady=20,command=lambda:btnCommand("-"))
btnV=Button(mansLogs, text="=", padx="40",pady=20,command=lambda:Equals())


e.grid(row=0,columnspan=4)
btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)
btnR.grid(row=1,column=3)

btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btnD.grid(row=2,column=3)

btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)
btnM.grid(row=3,column=3)

btn0.grid(row=4,column=1)
btnC.grid(row=4,column=0)
btnP.grid(row=4,column=3)
btnV.grid(row=4,column=2)

def btnClick(number):
    current=e.get() # nolasa skaitli
    e.delete(0,END) # nodzes
    newNumber=str(current)+str(number)
    e.insert(0,newNumber) # ievieto displeja
    return 0

def btnCommand(command):
    global number
    global num1
    global mathOp
    mathOp=command
    num1=int(e.get())
    e.delete(0,END)
    return 0

def Equals():
    num2=int(e.get())
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="-":
        result=num1-num2
    elif mathOp=="/":
        result=num1/num2
    elif mathOp=="*":
        result=num1*num2
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0

def Clear():
    e.delete(0,END)






mansLogs.mainloop()
