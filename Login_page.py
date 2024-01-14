from tkinter import*
from PIL import ImageTk
#Functionality part
def user_enter(event):
    if Username.get()=='Username':
        Username.delete(0,END)

def password_enter(event):
    if Password.get()=='Password':
        Password.delete(0,END)
        
def hide():
    openEye.config(file= "closeye.png")
    Password.config(show='*')
    eyeButton.config(command=show)

def show():
    openEye.config(file="openeye.png")
    Password.config(show='')
    eyeButton.config(command=hide)
        
#GUI part 

Login_Window =Tk()
Login_Window .geometry('990x660+50+50')
Login_Window.resizable(0,0)
Login_Window.title('Login Page')
bgImage=ImageTk.PhotoImage(file='bg.png')
bglabel=Label(Login_Window,image=bgImage)
bglabel.place(x=0,y=0)

headng = Label(Login_Window,text='User Login',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='firebrick1')
headng.place(x=605,y=120)

Username=Entry(Login_Window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
Username.place(x=590,y=200)
Username.insert(0,'Username')


Username.bind('<FocusIn>',user_enter)


Frame1=Frame(Login_Window,width=250,height=2,bg='firebrick1')
Frame1.place(x=590, y=225)

Password=Entry(Login_Window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
Password.place(x=590,y=260)
Password.insert(0,'Password')


Password.bind('<FocusIn>',password_enter)

Frame2=Frame(Login_Window,width=250,height=2,bg='firebrick1')
Frame2.place(x=590, y=282)

openEye=PhotoImage(file='openeye.png')
eyeButton = Button(Login_Window,image=openEye,bd =0,bg="white",activebackground="white",cursor="hand2",command=hide)
eyeButton.place(x=800,y=248)

Forget_Button = Button(Login_Window,text="Forgot Password",bd =0,bg="white",activebackground="white",cursor="hand2",font=('Microsoft Yahei UI Light',9,'bold'),fg='firebrick1')
Forget_Button.place(x=715,y=295)

loginButton =Button(Login_Window, text="Login", font=('open Sans',16,'bold'),fg='white',bg='firebrick1',activeforeground="white",activebackground="firebrick1",cursor='hand2',bd=0,width=19)
loginButton.place(x=578,y=350)


# orLabel =Label(Login_Window,text="-------------------OR------------------",font=('Open Sans',16),fg='firebrick1')
# orLabel

Login_Window.mainloop()