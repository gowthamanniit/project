import mysql.connector
import tkinter
from tkinter import *
from tkinter import messagebox
win=tkinter.Tk()
wi=win.winfo_screenwidth()
he=win.winfo_screenheight()
print(wi,he)
win.configure(width=wi,height=he,bg="green")
cf1=("times",30)
cf2=("Arial",15)

gen=StringVar()
gen.set("male")

co1=StringVar()
co2=StringVar()
co3=StringVar()
co4=StringVar()
co1.set("0")
co2.set("0")
co3.set("0")
co4.set("0")

def insfun():
    rno=int(rnotb.get())
    sname=snametb.get()
    address=addtb.get(0.0,"end")
    mark=int(marktb.get())
    gender=gen.get()
    cou=""
    if co1.get()=="1":
        cou=cou+"C "
    if co2.get()=="1":
        cou=cou+"C++ "
    if co3.get()=="1":
        cou=cou+"JAVA "
    if co4.get()=="1":
        cou=cou+"PYTHON "
    ph=phtb.get()
    messagebox.showinfo("rno:",rno)
    messagebox.showinfo("sname:",sname)
    messagebox.showinfo("add:",address)
    messagebox.showinfo("mark",mark)
    messagebox.showinfo("gender:",gender)
    messagebox.showinfo("course:",cou)
    messagebox.showinfo("phone:",ph)
    mycon=mysqlcon()
    qry="insert into student values(%d,'%s','%s',%d,'%s','%s','%s')"%(rno,sname,address,mark,gender,cou,ph)
    cur=mycon.cursor()
    cur.execute(qry)
    mycon.commit()
    messagebox.showinfo("success","inserted sucessfully, check db")
    canfun()
def delfun():
    rno=int(rnotb.get())
    mycon=mysqlcon()
    qry="delete from student where rno=%d"%rno
    cur=mycon.cursor()
    cur.execute(qry)
    mycon.commit()
    messagebox.showinfo("deleted","sucess")
def serfun():
    rno=int(rnotb.get())
    mycon=mysqlcon()
    qry="select * from student where rno=%d"%rno
    cur=mycon.cursor()
    cur.execute(qry)
    alldata=cur.fetchall()
    c=0
    for k in alldata:
        c=c+1
    if c==0:
        messagebox.showerror("No record:","Not found in db")
    else:
        for i in alldata:
            snametb.insert(0,i[1])
            addtb.insert(0.0,i[2])
            marktb.insert(0,i[3])
            gen.set(i[4])
            conlist=i[5].split(" ")
            for m in conlist:
                if m=="C":
                    co1.set("1")
                if m=="C++":
                    co2.set("1")
                if m=="JAVA":
                    co3.set("1")
                if m=="PYTHON":
                    co4.set("1")
                    
            phtb.insert(0,i[6])
            
    mycon.commit()



    
def mysqlcon():
    con=mysql.connector.connect(host="localhost",user="root",
                                password="12345",database="sproject")
    print("success")
    return con
    
def canfun():
    rnotb.delete(0,"end")
    snametb.delete(0,"end")
    addtb.delete(0.0,"end")
    marktb.delete(0,"end")
    co1.set(0)
    co2.set(0)
    co3.set(0)
    co4.set(0)
    phtb.delete(0,"end")

ptit=tkinter.Label(win,text="Student Application Form",font=cf1)

rnolbl=tkinter.Label(win,text="Enter roll number",font=cf2)
rnotb=tkinter.Entry(win,font=cf2)

snamelbl=tkinter.Label(win,text="Enter Student name:",font=cf2)
snametb=tkinter.Entry(win,font=cf2)

addlbl=tkinter.Label(win,text="Enter address",font=cf2)
addtb=tkinter.Text(win,height=5,width=20,font=cf2)

marklbl=tkinter.Label(win,text="Enter Mark:",font=cf2)
marktb=tkinter.Entry(win,font=cf2)

genlbl=tkinter.Label(win,text="Select Gender",font=cf2)
mrb=tkinter.Radiobutton(win,text="Male",font=cf2,variable=gen,value="male")
frb=tkinter.Radiobutton(win,text="FeMale",font=cf2,variable=gen,value="female")
orb=tkinter.Radiobutton(win,text="others",font=cf2,variable=gen,value="others")

clbl=tkinter.Label(win,text="Select Course:",font=cf2)
c1=tkinter.Checkbutton(win,text="C",font=cf2,variable=co1)
c2=tkinter.Checkbutton(win,text="C++",font=cf2,variable=co2)
c3=tkinter.Checkbutton(win,text="JAVA",font=cf2,variable=co3)
c4=tkinter.Checkbutton(win,text="PYTHON",font=cf2,variable=co4)

phlbl=tkinter.Label(win,text="Enter phone no:",font=cf2)
phtb=tkinter.Entry(win,font=cf2)

sbut=tkinter.Button(win,text="Insert/Save",font=cf2,command=insfun)
dbut=tkinter.Button(win,text="Delete",font=cf2,command=delfun)
serbut=tkinter.Button(win,text="Find",font=cf2,command=serfun)
cbut=tkinter.Button(win,text="Reset",font=cf2,command=canfun)

ptit.place(x=200,y=5)
rnolbl.place(x=100,y=100)
rnotb.place(x=300,y=100)
snamelbl.place(x=100,y=150)
snametb.place(x=300,y=150)
addlbl.place(x=100,y=200)
addtb.place(x=300,y=200)
marklbl.place(x=100,y=350)
marktb.place(x=300,y=350)
genlbl.place(x=100,y=400)
mrb.place(x=300,y=400)
frb.place(x=400,y=400)
orb.place(x=500,y=400)

clbl.place(x=100,y=450)
c1.place(x=300,y=450)
c2.place(x=400,y=450)
c3.place(x=500,y=450)
c4.place(x=600,y=450)
phlbl.place(x=100,y=500)
phtb.place(x=300,y=500)

sbut.place(x=300,y=550)
dbut.place(x=450,y=550)
serbut.place(x=650,y=550)
cbut.place(x=750,y=550)
win.mainloop()
