#!/usr/bin/env python
# coding: utf-8

# In[91]:


import time
import datetime
import sys
from tkinter import*


root =Tk()
root.title("Pyroll Systems")
root.geometry("1200x620+0+0")
#root.resizable(0,0)

Tops =Frame(root,width=1200,height=70,bd=10,relief="raise")
Tops.pack(side=TOP)

f1=Frame(root, width =600, height=600,bd=8,relief="raise")
f1.pack(side=LEFT)

f2=Frame(root, width =600, height=700,bd=8,relief="raise")
f2.pack(side=RIGHT)

f1a=Frame(f1,width =600,height=200,bd=20, relief="raise")
f1a.pack(side=TOP)

f1b=Frame(f1,width =600,height=600,bd=20,relief="raise")
f1b.pack(side=TOP)

lblinfo=Label(Tops, font=("Castellar",40,"bold") , text= " Payment Management System ", bd=8)
lblinfo.grid(row=0,column=0)

def reset():    
    Name.set("")
    Address.set("")
    Employer.set("")
    NI_Number.set("")
    Hours_Worked.set("")
    Hours_Rate.set("")
    Tax.set("")
    Over_Time.set("")
    Gross_Pay.set("")
    Net_Pay.set("")
    txtPaySlip.delete("1.0",END)
    

def iExit():
    root.destroy()
    return

def EnterInfo():
    txtPaySlip.insert(END, "\t   Pay Slip            \t\n")
    txtPaySlip.insert(END, "Name\t\t: "+Name.get()+"\n")
    txtPaySlip.insert(END, "Address\t\t: "+Address.get()+"\n")
    txtPaySlip.insert(END, "Employer\t\t: "+Employer.get()+"\n")
    txtPaySlip.insert(END, "NI Number\t\t: "+NI_Number.get()+"\n")
    txtPaySlip.insert(END, "Hours Worked\t\t: "+Hours_Worked.get()+"\n")
    txtPaySlip.insert(END, "Hours Rate\t\t: "+Hours_Rate.get()+"\n")
    txtPaySlip.insert(END, "Tax\t\t: "+Tax.get()+"\n")
    txtPaySlip.insert(END, "Over Time\t\t: "+Over_Time.get()+"\n")
    txtPaySlip.insert(END, "Gross Pay\t\t: "+Gross_Pay.get()+"\n")
    txtPaySlip.insert(END, "Net Pay\t\t: "+Net_Pay.get()+"\n")
    
    
def payment():
    HoursWorkedPerWeek=float(Hours_Worked.get())
    WagesPerHours=float(Hours_Rate.get())
    extra=float(Over_Time.get())

    overtime=extra*WagesPerHours    
    pay=WagesPerHours*HoursWorkedPerWeek
    paydue=pay+overtime
    PaymentDue =str ('%.2f'%(paydue))
    Gross_Pay.set(PaymentDue)
    
    tax = paydue*0.02
    Taxables=str('%.2f'%(tax))
    Tax.set(Taxables)
       
    netpay = paydue-tax
    NetPays=str('%.2f'%(netpay))
    Net_Pay.set(NetPays)
    
    
#----------------------------------------Defining Name--------------------------------------------#

Name=StringVar()
Address=StringVar()
Employer=StringVar()
NI_Number=StringVar()
Hours_Worked=StringVar()
Hours_Rate=StringVar()
Tax=StringVar()
Over_Time=StringVar()
Gross_Pay=StringVar()
Net_Pay=StringVar()
Dateoforder=StringVar()
Dateoforder.set(time.strftime("%d/%m/%Y"))

#---------------------------------------- Name Lables--------------------------------------------#

lblName=Label(f1a, text="NAME", font=("Times New Roman", 14,"bold"), bd=15).grid(row=0,column=0)
lblAddress=Label(f1a, text="ADDRESS", font=("Times New Roman", 14,"bold"), bd=15).grid(row=0,column=2)
lblEmployer=Label(f1a, text="EMPLOYER", font=("Times New Roman", 14,"bold"), bd=15).grid(row=1,column=0)
lblNI_Number=Label(f1a, text="NI NUMBER", font=("Times New Roman", 14,"bold"), bd=15).grid(row=1,column=2)
lblHours_Worked=Label(f1a, text="HOURS WORKED", font=("Times New Roman", 14,"bold"), bd=15).grid(row=2,column=0)
lblHours_Rate=Label(f1a, text="HOURS RATE", font=("Times New Roman", 14,"bold"), bd=15).grid(row=2,column=2)
lblTax=Label(f1a, text="TAX", font=("Times New Roman", 14,"bold"), bd=15).grid(row=3,column=0)
lblOver_Time=Label(f1a, text="OVER TIME", font=("Times New Roman", 14,"bold"), bd=15).grid(row=3,column=2)
lblGross_Pay=Label(f1a, text="GROSS PAY", font=("Times New Roman", 14,"bold"), bd=15).grid(row=4,column=0)
lblNet_Pay=Label(f1a, text="NET PAY", font=("Times New Roman", 14,"bold"), bd=15).grid(row=4,column=2)

#---------------------------------------- Text Box--------------------------------------------#

etxtName=Entry(f1a, textvariable=Name,font=("Courier New", 16,"bold"),bd=16,width=15, justify="left")
etxtName.grid(row=0, column=1)

etxtAddress=Entry(f1a, textvariable=Address,font=("Courier New", 16,"bold"),bd=16,width=15, justify="left")
etxtAddress.grid(row=0, column=3)

etxtEmployer=Entry(f1a, textvariable=Employer,font=("Courier New", 16,"bold"),bd=16,width=15, justify="left")
etxtEmployer.grid(row=1, column=1)

etxtNI_Number=Entry(f1a, textvariable=NI_Number,font=("Courier New", 16,"bold"),bd=16,width=15, justify="left")
etxtNI_Number.grid(row=1, column=3)

etxtHours_Worked=Entry(f1a, textvariable=Hours_Worked,font=("Courier New", 16,"bold"),bd=16,width=15, justify="left")
etxtHours_Worked.grid(row=2, column=1)

etxtHours_Rate=Entry(f1a, textvariable=Hours_Rate,font=("Courier New", 16,"bold"),bd=16,width=15, justify="left")
etxtHours_Rate.grid(row=2, column=3)

etxtTax=Entry(f1a, textvariable=Tax,font=("Courier New", 16,"bold"),bd=16,width=15, justify="left")
etxtTax.grid(row=3, column=1)

etxtOver_Time=Entry(f1a, textvariable=Over_Time,font=("Courier New", 16,"bold"),bd=16,width=15, justify="left")
etxtOver_Time.grid(row=3, column=3)

etxtGross_Pay=Entry(f1a, textvariable=Gross_Pay,font=("Courier New", 16,"bold"),bd=16,width=15, justify="left")
etxtGross_Pay.grid(row=4, column=1)

etxtNet_Pay=Entry(f1a, textvariable=Net_Pay,font=("Courier New", 16,"bold"),bd=16,width=15, justify="left")
etxtNet_Pay.grid(row=4, column=3)

lblPaySlip=Label(f2,textvariable=Dateoforder, font=("Courier New", 21, "bold")).grid(row=0, column=0)

txtPaySlip=Text(f2,height=19,width=20,bd=16, font=("Courier New", 14, "bold"))
txtPaySlip.grid(row=1, column=0)

btnsalary=Button(f1b, text="Weekly Salary", padx=17,pady=16,bd=8,fg="black",
    font=("Castellar",13,"bold"),width=10,height=1, command=payment).grid(row=0,column=0)

btnReset=Button(f1b, text="Reset", padx=17,pady=16,bd=8,fg="black",
    font=("Castellar",13,"bold"),width=10,height=1,command=reset).grid(row=0,column=1)
    
btnView_Payslip=Button(f1b, text="View Payslip", padx=17,pady=16,bd=8,fg="black", 
    font=("Castellar",13,"bold"),width=10,height=1,command=EnterInfo).grid(row=0,column=2)

btnExit_System=Button(f1b, text="Exit System", padx=17,pady=16,bd=8,fg="black", 
    font=("Castellar",13,"bold"),width=10,height=1, command=iExit).grid(row=0,column=3)
    
root.mainloop()

