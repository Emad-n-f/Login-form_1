from tkinter import * 
from tkinter import messagebox 
from class_bank import *
#from def_bank import *


win = Tk()
ars = 400
toll = 330
w = win.winfo_screenwidth()
h = win.winfo_screenheight()
ww = (w // 2) - (ars // 2)
hh = (h // 2) - (toll // 2)

win.geometry(f'{ars}x{toll}+{ww}+{hh}')
win.resizable(0,0)
win.title('Emad noudeh farahani')

db1 = database('d:/python_3/bank_db4.db')

#_________Functian
def s_up():
    name = ent_Fname.get()
    lname = ent_lname.get()
    email1 = ent_email.get()
    pas = ent_pass.get()
    email = email1.lower()
    x = db1.select_info()
    is_email = False
    for i in x:
        if email == i[3]:
            is_email = True
            break
            
    if email == '' or pas == '':
        messagebox.showerror("خطا",'فیلد ایمیل و پسورد اجباری!')
    elif '@' not in email or '.com' not in email:
        messagebox.showerror("خطا", "ایمیل نامعتبر است")
    elif is_email:
        messagebox.showerror('خطا','این ایمیل از قبل وجود دارد')
    else:
        db1.insert_info(name,lname,email,pas)
        messagebox.showinfo('تمام','اطلاعات با موفقیت اضافه شدند')
        clear()
            


def s_in():
    name = ent_Fname.get()
    lname = ent_lname.get()
    emai = ent_email.get()
    pas = ent_pass.get()
    x = db1.select_info()
    email = emai.lower()
    global user
    user = []
    is_info = False
    for i in x:
            if i[3] == email and i[4] == pas:
                user = i
                is_info = True
                break
    if is_info:
        messagebox.showinfo('تمام','ورود موفقیت آمیز بود')
        clear()
        win.withdraw()
        win_oo(user)
    elif is_info == False:
        messagebox.showerror('خطا','رمز یا ایمیل اشتباه!')
    elif email == '' or pas == '':
        messagebox.showerror("خطا",'فیلد ایمیل و پسورد اجباری !')

    else:
        messagebox.showinfo('خطا','کاربر یافت نشد !')
        clear()

        
def clear():
    ent_Fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_email.delete(0,END)
    ent_pass.delete(0,END)

def win_oo(infor):
    global name_info
    id = infor[0]
    name_info = infor[1]
    lname = infor[2]
    email = infor[3]
    pas = infor[4]

    global clear_oo,close_oo
    def clear_oo():
        ent_rename.delete(0,END)
        ent_relname.delete(0,END)
        pass

    def sin_out():
        a = messagebox.askyesno('Are you sure?','You want sing out from your account?')
        if a:
           close_oo()
        pass

    def close_oo():
        oo.withdraw()
        win.deiconify()

    def exit_oo():
        x = messagebox.askyesno('میخوای خارج شی؟','آیا میخوای به طور کامل از برنامه خارج شی؟')
        if x:
            oo.destroy()
            win.destroy()
            ch_pas_1.destroy()
            ch_email_1.destroy()
        pass

    global lbl_wellcome , lst_info
    oo = Toplevel(win)
    ars1 = 400
    toll1 = 620
    w1 = oo.winfo_screenwidth()
    h1 = oo.winfo_screenheight()
    ww1 = (w1 // 2) - (ars1 // 2)
    hh1 = (h1 // 2) - (toll1 // 2)
    oo.geometry(f'{ars1}x{toll1}+{ww1}+{hh1}')


    lbl_wellcome = Label(oo,text=f'Well come {name_info}',font='arial 12',fg='blue')
    lbl_wellcome.pack(pady=5)
    lbl_rename = Label(oo,text='New name :').place(x=20,y=80)
    lbl_relname = Label(oo,text='New Lname :').place(x=20,y=120)

    global ent_relname,ent_rename
    ent_rename = Entry(oo)
    ent_rename.place(x=100,y=80)
    ent_relname = Entry(oo)
    ent_relname.place(x=100,y=120)
    

    btn_rename = Button(oo,text='Rename',width=10,command=lambda:rename(ent_rename.get(),id))
    btn_rename.place(x=250,y=77)
    btn_rename = Button(oo,text='ReLname',width=10,command=lambda:relname(ent_relname.get(),id))
    btn_rename.place(x=250,y=117)
    btn_show_info = Button(oo,text='Show my informatian in list',width=22,height=2,bg='green',command=show_info_lst)
    btn_show_info.place(x=125,y=420)
    btn_show_info2 = Button(oo,text='Show my informatian in box',width=22,height=2,bg='blue',command=show_info_mes)
    btn_show_info2.place(x=125,y=470)

    btn_ch_pas = Button(oo,text='Change Password',height=2,width=16,command=ch_pas)
    btn_ch_pas.place(x=60,y=170)
    btn_ch_email = Button(oo,text='Change Email',height=2,width=16,command=ch_email)
    btn_ch_email.place(x=220,y=170)

    btn_out = Button(oo,text='Sing out',height=2,command=sin_out)
    btn_out.place(x=20,y=560)
    btn_delete = Button(oo,text='Delete My account',width=15,height=2,command=delete_account)
    btn_delete.place(x=140,y=560)
    btn_exit_oo = Button(oo,text='Exit',height=2,width=10,command=exit_oo)
    btn_exit_oo.place(x=300,y=560)

    lst_info = Listbox(oo,width=50)
    lst_info.pack(padx=10,pady=190)

    s_bar = Scrollbar(oo)
    s_bar.place(x=355,y=224,height=170)
    lst_info.config(yscrollcommand=s_bar.set)
    s_bar.config(command=lst_info.yview)

    #این بخش کامل نیست
    #s_bar1 = Scrollbar(oo)
    #s_bar1.place(x=10,y=394,width=120)
    #lst_info.config(xscrollcommand=s_bar1.set)
    #s_bar1.config(command=lst_info.xview)

    
    #oo.mainloop()



def ch_pas():
    #پنجره تغییر رمز
    global ch_pas_1
    ch_pas_1 = Toplevel()
    ars1 = 320
    toll1 = 180
    w1 = ch_pas_1.winfo_screenwidth()
    h1 = ch_pas_1.winfo_screenheight()
    ww1 = (w1 // 2) - (ars1 // 2)
    hh1 = (h1 // 2) - (toll1 // 2)
    ch_pas_1.geometry(f'{ars1}x{toll1}+{ww1}+{hh1}')

    ch_pas_1.title('Change Password')

    def exit_1():
        x = messagebox.askyesno("هشدار",'آیا میخوای از این بخش خارج بشی؟')
        if x:
            ch_pas_1.withdraw()
                    
        pass

    def ch_btn():
        x = db1.select_info()
        info_karbar = ''
        id_karbar = user[0]
        for i in x:
            if i[0] == id_karbar:
                info_karbar = i
        cur_pass = ent_cur_pass.get()
        new_pass = ent_new_pass.get()
        renew_pass = ent_renew_pass.get()
        if cur_pass == '':
                    messagebox.showerror('خطا',"""فیلد رمز خالی میباشد 
                    لطفا رمز فعلی اکانت خود را وارد کنید""")
                    pass
        elif cur_pass != info_karbar[4]:
            messagebox.showerror('خطا','! رمز فعلی اشتباه است')
            pass
        elif new_pass != renew_pass:
            messagebox.showerror('خطا','! رمز جدید در هر دو فیلد یکسان نیست')
            pass
        elif new_pass == '' or renew_pass == '':
            messagebox.showerror('خطا',' !فیلد رمز جدید خالی میباشد')
            pass
        elif cur_pass == new_pass:
            txt = f""" هست {new_pass} رمز فعلی شما هم اکنون
            اگر میخواهید رمزتان را تغییر دهید رمز جدیدی وارد کنید """
            messagebox.showerror('',txt)
            pass
        else:
            db1.edit_pass(new_pass,id_karbar)
            text_new_pass = f''' رمز شما با موفقیت تغییر یافت 
            رمز جدید شما : {new_pass}'''
            messagebox.showinfo('انجام شد',text_new_pass)
            ent_cur_pass.delete(0,END)
            ent_new_pass.delete(0,END)
            ent_renew_pass.delete(0,END)
            ch_pas_1.withdraw()
            pass
        

    ent_cur_pass = Entry(ch_pas_1)
    ent_cur_pass.place(x=170,y=10)
    ent_new_pass = Entry(ch_pas_1)
    ent_new_pass.place(x=170,y=35)
    ent_renew_pass = Entry(ch_pas_1)
    ent_renew_pass.place(x=170,y=60)


    lbl_cur_pas = Label(ch_pas_1,text='Enter current Password :').place(x=20,y=10)
    lb1_new_pas = Label(ch_pas_1,text='Enter a new password :').place(x=20,y=35)
    lb1_renew_pas = Label(ch_pas_1,text='Re-enter new password :').place(x=20,y=60)

    btn_changes = Button(ch_pas_1,text='Saving Changes',height=2,width=12,command=ch_btn)
    btn_changes.place(x=50,y=110)
    btn_exit = Button(ch_pas_1,text=('Exit'),height=2,width=12,command=exit_1)
    btn_exit.place(x=190,y=110)
    # پایان پنجره تغییر رمز

def ch_email():
    global ch_email_1
    ch_email_1 = Toplevel()
    ars1 = 320
    toll1 = 180
    w1 = ch_email_1.winfo_screenwidth()
    h1 = ch_email_1.winfo_screenheight()
    ww1 = (w1 // 2) - (ars1 // 2)
    hh1 = (h1 // 2) - (toll1 // 2)
    ch_email_1.geometry(f'{ars1}x{toll1}+{ww1}+{hh1}')

    ch_email_1.title('Change Email')

    ent_cur_pass1 = Entry(ch_email_1)
    ent_cur_pass1.place() 

    def exit_2():
        x = messagebox.askyesno("هشدار",'آیا میخوای از این بخش خارج بشی؟')
        if x:
            ch_email_1.withdraw()

    def ch_btn1():
        x = db1.select_info()
        info_karbar = ''
        id_karbar = user[0]
        for i in x:
            if i[0] == id_karbar:
                info_karbar = i
        cur_pass = ent_cur_pass1.get()
        new_email = ent_new_email.get()
        renew_email = ent_renew_email.get()
        if cur_pass == '':
            messagebox.showerror('خطا',"""فیلد رمز خالی میباشد 
            لطفا رمز فعلی اکانت خود را وارد کنید""")
            pass
        elif cur_pass != info_karbar[4]:
            messagebox.showerror('خطا','! رمز فعلی اشتباه است')
            pass
        elif '@' not in new_email or '.com' not in new_email:
            messagebox.showerror("خطا", "ایمیل نامعتبر است")
            pass
        elif new_email != renew_email:
            messagebox.showerror('خطا','! ایمیل جدید در هر دو فیلد یکسان نیست')
            pass
        elif new_email == '' or renew_email == '':
            messagebox.showerror('خطا',' !فیلد ایمیل جدید خالی میباشد')
            pass
        elif info_karbar[3] == new_email:
            txt = f""" هست {new_email} ایمیل فعلی شما هم اکنون
             اگر میخواهید ایمیلتان را تغییر دهید ایمیل جدیدی وارد کنید """
            messagebox.showerror('',txt)
            pass
        else:
            db1.edit_email(new_email,id_karbar)
            text_new_pass = f''' ایمیل شما با موفقیت تغییر یافت 
             ایمیل جدید شما : {new_email}'''
            messagebox.showinfo('انجام شد',text_new_pass)
            ent_cur_pass1.delete(0,END)
            ent_new_email.delete(0,END)
            ent_renew_email.delete(0,END)
            ch_email_1.withdraw()
            pass


    ent_cur_pass1 = Entry(ch_email_1)
    ent_cur_pass1.place(x=170,y=10)
    ent_new_email = Entry(ch_email_1)
    ent_new_email.place(x=170,y=35)
    ent_renew_email = Entry(ch_email_1)
    ent_renew_email.place(x=170,y=60)


    lbl_cur_pas = Label(ch_email_1,text='Enter current Password :').place(x=20,y=10)
    lb1_new_email = Label(ch_email_1,text='Enter a new Email:').place(x=20,y=35)
    lb1_renew_email = Label(ch_email_1,text='Re-enter new Email :').place(x=20,y=60)

    btn_changes1 = Button(ch_email_1,text='Saving Changes',height=2,width=12,command=ch_btn1)
    btn_changes1.place(x=50,y=110)
    btn_exit1 = Button(ch_email_1,text=('Exit'),height=2,width=12,command=exit_2)
    btn_exit1.place(x=190,y=110)
    
def delete_account():
    id = user[0]
    x = messagebox.askyesno('هشدار',"""میخوای اکانتت کاملا حذف بشه؟
    این کار همه اطلاعات شمارو پاک میکنه و قابل برگشت نیست""")
    if x:
        db1.delete_info(id)
        close_oo()
    pass

def fetch():
    pass

def rename(name,id):
    if name == '':
        messagebox.showerror('خطایی رخ داد','فیلد اسم خالی میباشد!')
    else:
        db1.edit_name(name,id)
        lbl_wellcome.configure(text=f'Well come {name}',font='arial 12',fg='blue')
        messagebox.showinfo('انجام شد',' اسم حساب شما با موفقیت ویرایش شد')
        clear_oo()
        name_info = name

def relname(lname,id):
    if lname == '':
        messagebox.showerror("خطایی رخ داد","فیلد نام خانوادگی خالی میباشد!")
    else:
        db1.edit_lname(lname,id)
        messagebox.showinfo('انجام شد',' نام خانوادگی حساب شما با موفقیت ویرایش شد')
        clear_oo()

def show_pas(event):
    a = ent_pass.get()
    if a == '':
        messagebox.showerror('Error!','password is empty!')
    else:
        messagebox.showinfo('your password',f'Your password : {a}')

def show_info_lst():
    id_karbar = user[0]
    x = db1.select_info()
    for i in x:
        if i[0] == id_karbar:
            userr = i
    id = userr[0]
    fname = userr[1]
    lname = userr[2]
    email = userr[3]
    pas = userr[4]
    lst_info.insert(END,f'~~~ Your  informatian  in  app ~~~')
    lst_info.insert(END,f'First name : {fname} <--> Last name : {lname}')
    lst_info.insert(END,f'Email : {email} <--> Pass word : {pas}')
def show_info_mes():
    id_karbar = user[0]
    x = db1.select_info()
    for i in x:
        if i[0] == id_karbar:
            userr = i
    id = userr[0]
    fname = userr[1]
    lname = userr[2]
    email = userr[3]
    pas = userr[4]
    a = f''' Your informatian in app
    First name : {fname} <--> Last name : {lname}
    Email : {email}
    Pass word : {pas}''' 
    messagebox.showinfo("Informatian",a)
    

lbll_fname = Label(win,text='fname : ',font='arial 12 ').place(x=80,y=10)
lbll_lname = Label(win,text='lname : ',font='arial 12 ').place(x=80,y=40)
lbll_email = Label(win,text='email : ',font='arial 12 ').place(x=80,y=70)
lbll_password = Label(win,text='password : ',font='arial 12 ').place(x=65,y=100)
lbll_email = Label(win,text='*' , fg = 'red',font='arial 12 ').place(x=70,y=70)
lbll_password = Label(win,text='*' , fg = 'red',font='arial 12 ').place(x=55,y=100)
lbl_show_pas = Label(win,text='show password')
lbl_show_pas.place(x=288,y=102)

ent_Fname = Entry(win)
ent_Fname.place(y = 15 , x = 160)
ent_lname = Entry(win)
ent_lname.place(y = 45 , x = 160)
ent_email = Entry(win)
ent_email.place(y = 75 , x = 160)
ent_pass = Entry(win,show='*')
ent_pass.place(y = 105 , x = 160)
lbl_show_pas.bind('<Button-1>',show_pas)
btn_up = Button(win , text = 'Sign up' , width= 12 , height=2,command=s_up).place(x = 85 , y = 180)
btn_in = Button(win , text = 'Sign in' , width= 12 , height=2,command=s_in).place(x = 220, y = 180)



win.mainloop()
