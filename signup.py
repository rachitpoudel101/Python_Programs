from tkinter import*
from PIL import ImageTk
#Functionality part


#GUI part 

Signup_Window =Tk()
Signup_Window.title('Sign Up Page')
Signup_Window.resizable(False,False)
bgImage=ImageTk.PhotoImage(file='bg.png')
bglabel=Label(Signup_Window,image=bgImage)
bglabel.grid()

frame =Frame(Signup_Window,bg= 'white')
frame.place(x=554 ,y= 100)

headng = Label(frame,text='CREATE AN ACCOUNT',font=('Microsoft Yahei UI Light',18,'bold'),bg='white',fg='firebrick1')
headng.grid(row=0 ,column=0,padx=10,pady=10)

emaillabel =Label(frame,text='Email',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
emaillabel.grid(row=1,column=0, sticky='w',padx=25,pady=(10,0))
emailentry =Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
emailentry.grid(row=2,column=0,sticky='w',padx=25)

usernamelabel =Label(frame,text='Username',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
usernamelabel.grid(row=3,column=0, sticky='w',padx=25,pady=(10,0))
usernameentry =Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
usernameentry.grid(row=4,column=0,sticky='w',padx=25)

Passwordlabel =Label(frame,text='Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
Passwordlabel.grid(row=5,column=0, sticky='w',padx=25,pady=(10,0))
Passwordentry =Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
Passwordentry.grid(row=6,column=0,sticky='w',padx=25)

Conpasswordlabel =Label(frame,text='Confirm Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
Conpasswordlabel.grid(row=7,column=0, sticky='w',padx=25,pady=(10,0))
Conpasswordentry =Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
Conpasswordentry.grid(row=8,column=0,sticky='w',padx=25)


Signup_Window.mainloop()