
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

myform = tkinter.Tk()
myform.title(" المبادره السعوديه للمطورين")
myform.geometry('700x500')
lbl1 = ttk.Label( myform, text = ' We Can Do it',font=('impact', 16))
lbl1.grid(row=2, column=1)
# اعدادت صورة اللعبه
path = "small.jpg"
img = ImageTk.PhotoImage(Image.open(path))
panel = Label(myform, image=img, width=300)
panel.grid(row=3, column=1, padx=10)

myform.mainloop()





