from tkinter import*
from PIL import ImageTk

root =Tk()
root .geometry('990x660+50+50')

bgImage=ImageTk.PhotoImage(file='bg.png')
bglabel=Label(root,image=bgImage)
bglabel.place(x=0,y=0)

headng = Label(root,text='User Login')
headng.place(x=605,y=120)
root.mainloop()