from tkinter import *
import tkinter as tk 
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root .title("Weather App")
root.geometry( "900x500+300+200")
root.resizable(False,False)


#Searched box
Search_image=PhotoImage(file="search.png")
myimage = Label(image=Search_image)
myimage.place(x=20,y=20)


textfeild=tk.Entry(root,justify="center",width=20, font=("popins",25,"bold"),bg="#404040",border=2,fg="red")
textfeild.place(x=50,y=40)
textfeild.focus()


Searched_icon=PhotoImage(file="search_icon.png")
myimage_icon =Button(image=Searched_icon, borderwidth=0,cursor="hand2",bg="#404040")
myimage_icon.place(x=400,y=34)

#logo
logo_image=PhotoImage(file="logo.png")
logo=Label(image=logo_image)
logo.place(x=150, y=100)




root.mainloop()