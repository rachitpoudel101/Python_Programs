from tkinter import*
from PIL import ImageTk

root =Tk()


bgImage=ImageTk.PhotoImage(file='bg.png')
bglabel=Label(root,image=bgImage)
bglabel.grid(row=0,column=0)
root.mainloop()