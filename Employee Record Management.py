from tkinter import *
from tkinter import ttk,messagebox
import os
root=Tk()

root.title('Employee Record')
root.geometry('1100x650')
bg_color="#1974d2"

#----variables----=
id_var=IntVar()
name_var=StringVar()
fname_var=StringVar()
gender_var=StringVar()
email_var=StringVar()
salary_var=StringVar()
phone_var=IntVar()
desi_var=StringVar()

#===Function----
def add():
    if id_var.get()=='0' or name_var.get()=='' or fname_var.get()=='' or gender_var.get()=='' or email_var.get()=='' or salary_var.get()=='' or phone_var.get()=='' or desi_var.get()=='':

        messagebox.showerror('Error','All fileds are required ?')
    else:
        textarea.delete(1.0,END)
        textarea.insert(END, '\n===================================================')
        textarea.insert(END,f'Employee Id\t\t\t\t{id_var.get()}')
        textarea.insert(END, '\n====================================================')
        textarea.insert(END, f'\n\nFull Name\t\t\t\t{name_var.get()}')
        textarea.insert(END, f'\nFather Name\t\t\t\t{fname_var.get()}')
        textarea.insert(END, f'\nEmail Id\t\t\t\t{email_var.get()}')
        textarea.insert(END, f'\nGender\t\t\t\t{gender_var.get()}')
        textarea.insert(END, f'\nDesignation\t\t\t\t{desi_var.get()}')
        textarea.insert(END, f'\nContact No.\t\t\t\t{phone_var.get()}')
        textarea.insert(END, f'\nSalary\t\t\t\t{salary_var.get()}')
        textarea.insert(END, f'\nAddress\t\t\t\t{txt_add.get(1.0,END)}')
        textarea.insert(END, '\n\n###########################################################')

def Save():
    data=textarea.get(1.0,END)
    F1=open('Employee Records/'+str(id_var.get())+'.txt','w')
    F1.write(data)
    F1.close()
    messagebox.showinfo('Saved',f'Employee Id:{id_var.get()}Saved Successfully')

def Print():
    data=textarea.get(1.0,END)
    f='C:\\Users\\HP\\PycharmProjects\\pythonProject1\\Employee Records\\'+str(id_var.get())+'.txt'
    os.startfile(f,'Print')

def Reset():
        textarea.delete(1.0,END)
        txt_add.delete(1.0,END)
        id_var.set(0)
        name_var.set('')
        fname_var.set('')
        gender_var.set('')
        desi_var.set('')
        phone_var.set('')
        email_var.set('')
        salary_var.set('')

def Exit():
    if messagebox.askyesno('Exit','Do you want to exit'):
        root.destroy()

#----------Headline----
title =Label(root,text='Employee Records System',bg=bg_color,fg='white',font=('time rommmon',23,'bold'),relief=GROOVE,bd=4)
title.pack(fill=X)

#--------left frame details====
F1=Frame(root,bg=bg_color,relief=RIDGE,bd=3)
F1.place(x=1,y=46,width=625,height=510)

lbl_id=Label(F1,text='Employee Id',font=('time rommon',14,'bold'),fg='black',bg=bg_color)
lbl_id.grid(row=0,column=0,padx=30,pady=10)
txt_id=Entry(F1,font=('time rommon',12,'bold'),relief=RIDGE,bd=2,textvariable=id_var)
txt_id.grid(row=0,column=1,pady=10,sticky='w')

lbl_name=Label(F1,text='Full Name     ',font=('time rommon',14,'bold'),fg='black',bg=bg_color)
lbl_name.grid(row=1,column=0,padx=30,pady=10)
txt_name=Entry(F1,font=('time rommon',12),relief=RIDGE,bd=2,textvariable=name_var)
txt_name.grid(row=1,column=1,pady=10,sticky='w')

lbl_fname=Label(F1,text='Father Name',font=('time rommon',14,'bold'),fg='black',bg=bg_color)
lbl_fname.grid(row=2,column=0,padx=30,pady=10)
txt_fname=Entry(F1,font=('time rommon',12),relief=RIDGE,bd=2,textvariable=fname_var)
txt_fname.grid(row=2,column=1,pady=10,sticky='w')


lbl_email=Label(F1,text='Email ID        ',font=('time rommon',14,'bold'),fg='black',bg=bg_color)
lbl_email.grid(row=3,column=0,padx=30,pady=10)
txt_email=Entry(F1,font=('time rommon',12),relief=RIDGE,bd=2,textvariable=email_var)
txt_email.grid(row=3,column=1,pady=10,sticky='w')

lbl_gender=Label(F1,text='Gender          ',font=('time rommon',14,'bold'),fg='black',bg=bg_color)
lbl_gender.grid(row=4,column=0,padx=30,pady=10)

combo_gender=ttk.Combobox(F1,font=('time rommon',14,),state='readonly',textvariable=gender_var)
combo_gender['value']=('Male','Female','Other')
combo_gender.grid(row=4,column=1,pady=8)

lbl_des=Label(F1,text=' Designation  ',font=('time rommon',14,'bold'),fg='black',bg=bg_color)
lbl_des.grid(row=5,column=0,padx=30,pady=10)

combo_des=ttk.Combobox(F1,font=('time rommon',14,),state='readonly',textvariable=desi_var)
combo_des['value']=('HR','Accountant','Sale','IT','Management','Legal')
combo_des.grid(row=5,column=1,pady=8)

lbl_no=Label(F1,text=' Contact No.   ',font=('time rommon',14,'bold'),fg='black',bg=bg_color)
lbl_no.grid(row=6,column=0,padx=30,pady=10)
txt_no=Entry(F1,font=('time rommon',12,),relief=RIDGE,bd=2,textvariable=phone_var)
txt_no.grid(row=6,column=1,pady=10,sticky='w')

lbl_salary=Label(F1,text='Salary           ',font=('time rommon',14,'bold'),fg='black',bg=bg_color)
lbl_salary.grid(row=7,column=0,padx=30,pady=10)
txt_salary=Entry(F1,font=('time rommon',12,),relief=RIDGE,bd=2,textvariable=salary_var)
txt_salary.grid(row=7,column=1,pady=10,sticky='w')

lbl_add=Label(F1,text='Address      ',font=('time rommon',14,'bold'),fg='black',bg=bg_color)
lbl_add.grid(row=8,column=0,padx=30,pady=10)
txt_add=Text(F1,width=30,height=2,font=('time rommon',12,),relief=RIDGE,bd=2,)
txt_add.grid(row=8,column=1,pady=5,sticky='w')


#--------Right frame details--==
F2=Frame(root,bg='white',relief=RIDGE,bd=3)
F2.place(x=626,y=46,width=650,height=510)

lbl_t=Label(F2,text='Employee Details',font=('arial 15 bold'),fg='black',bd=2,relief=GROOVE)
lbl_t.pack(fill=X)

scrol=Scrollbar(F2,orient=VERTICAL)
scrol.pack(side=RIGHT,fill=Y)
textarea=Text(F2,font='arial 15',yscrollcommand=scrol.set)
textarea.pack(fill=BOTH)
scrol.config(command=textarea.yview())

# ----buthons===
F3=Frame(root,bg=bg_color,relief=RIDGE,bd=2)
F3.place(x=1,y=550,width=1275,height=100)

btn1=Button(F3,text='Add Record',font='arial 16 bold',bg='#ff4500',fg='white',width=10,command=add)
btn1.grid(row=0,column=0,padx=32,pady=7)

btn2=Button(F3,text='Save',font='arial 16 bold',bg='#006400',fg='white',width=10,command=Save)
btn2.grid(row=0,column=1,padx=55,pady=7)

btn3=Button(F3,text='Print',font='arial 16 bold',bg='#39ff14',fg='white',width=10,command=Print)
btn3.grid(row=0,column=2,padx=72,pady=7)

btn4=Button(F3,text='Reset',font='arial 16 bold',bg='#ff4500',fg='white',width=10,command=Reset)
btn4.grid(row=0,column=3,padx=73,pady=7)

btn5=Button(F3,text='Exit',font='arial 16 bold',bg='Red',fg='white',width=10,command=Exit)
btn5.grid(row=0,column=4,padx=78,pady=7)


mainloop()