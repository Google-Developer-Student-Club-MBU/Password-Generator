import tkinter as tk
import random as rd
from tkinter import messagebox
password=tk.Tk()
password.title("PASSWORD GENERATOR.")
password.geometry("500x500")

def generate_password():
    c_1=var1.get()
    c_2=var2.get()
    if c_1=="" or c_2==0 :
        messagebox.showerror("SELECTION ERROR ","SELECT THE OPTIONS & PRESS GENERATE.")
    else:
        alp_l="abcdefghijklmnopqrstuvwxyz"
        alp_h=alp_l.upper()
        symbols="!@$%*&#"
        total=alp_l+alp_h+symbols
        numbers="1234567890"
        if c_1=="ALPHANUMERIC":
            temp=rd.sample(total+numbers,c_2)
            result_1="".join(temp)
        elif c_1=="ONLY WITH NUMBERS":
            temp=rd.sample(numbers,c_2)
            result_1="".join(temp)    
        result.config(text=f"                             YOUR PASSWORD: {result_1}                       ")
frame=tk.LabelFrame(text="GENERATE YOUR PASSWORDS : ")
frame.place(x=100,y=100)

select1=tk.Label(frame,text="SELECT THE TYPE OF PASSWORD.")
select1.pack()

s1=["ALPHANUMERIC","ONLY WITH NUMBERS"]
var1=tk.StringVar()
option1=tk.OptionMenu(frame,var1,*s1)
option1.pack()

select2=tk.Label(frame,text="SELECT THE LENGTH OF PASSWORD.")
select2.pack()

s2=[6,7,8]
var2=tk.IntVar()
option2=tk.OptionMenu(frame,var2,*s2)
option2.pack()

result=tk.Label(frame,text=" SELECT OPTIONS & CLICK ON GENERATE PASSWORD.")
result.pack()

result_b=tk.Button(frame,text="GENERATE PASSWORD.",command=generate_password)
result_b.pack()
emp=tk.Label(frame,text="     ")
emp.pack()
password.mainloop()