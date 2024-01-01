from tkinter import*
from PIL import ImageTk
#Functionality part
def on_enter(event):
    if Username.get()=='Username':
        Username.delete(0,END)
        
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


Username.bind('<FocusIn>',on_enter)


Frame(Login_Window,width=250,height=2,bd=0,fg='firebrick1').place(x=590, y=225)

Login_Window.mainloop()