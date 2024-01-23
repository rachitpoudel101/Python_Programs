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
emaillabel.grid(row=1,column=0, sticky='w',padx=25)
emailentry =Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'))
emailentry.grid(row=2,column=0,sticky='w',padx=25)

Signup_Window.mainloop()