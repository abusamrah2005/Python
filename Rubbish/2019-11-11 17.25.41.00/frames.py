# from tkinter import *


# def raise_frame(frame):
#     frame.tkraise()

# root = Tk()

# f1 = Frame(root)
# f2 = Frame(root)
# f3 = Frame(root)
# f4 = Frame(root)

# for frame in (f1, f2, f3, f4):
#     frame.grid(row=0, column=0, sticky='news')

# Button(f1, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()
# Label(f1, text='FRAME 1').pack()

# Label(f2, text='FRAME 2').pack()
# Button(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()

# Label(f3, text='FRAME 3').pack(side='left')
# Button(f3, text='Go to frame 4', command=lambda:raise_frame(f4)).pack(side='left')

# Label(f4, text='FRAME 4').pack()
# Button(f4, text='Goto to frame 1', command=lambda:raise_frame(f1)).pack()

# raise_frame(f1)
# root.mainloop()

# from tkinter import *

# root = Tk(className = "button_click_label")
# root.geometry("200x200")

# message = StringVar()
# message.set('hi')

# l1 = Label(root, text="hi")


# bb = Entry(root).pack()
# def press():
#     l1.config(text="hello")
# def press1():
#     l1.config(text="eeee")

# b1 = Button(root, text = "clickhere", command = press).pack()
# b2 = Button(root, text = "clickhere", command = press1).pack()

# l1.pack()


# def say_hello():
#     name_of_user = entry_1.get()
#     string_to_display = name_of_user
#     var_1.set(string_to_display)
#     # label_2["text"] = string_to_display

# var_1 = StringVar()
# label_1 = Label(root, text="Enter name")
# entry_1 = Entry(root)
# button_1 = Button(root, text="Click Me", command=say_hello)
# label_2 = Label(root, textvariable=var_1)

# label_1.grid(row=0, column=0)
# entry_1.grid(row=0, column=1)
# button_1.grid(row=1, column=0)
# label_2.grid(row=1, column=1)
# root.mainloop()



from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import messagebox



saudidevorg = Tk()
width_of_window = 820
height_of_window = 600
screen_width = saudidevorg.winfo_screenwidth()
screen_height = saudidevorg.winfo_screenheight()
x_coordinate = (screen_width/2) - (width_of_window/2)
y_coordinate = (screen_height/2) - (height_of_window/2)
saudidevorg.geometry("%dx%d+%d+%d" % (width_of_window,
                                      height_of_window, x_coordinate, y_coordinate))
saudidevorg.title(" المبادرة السعودية للمطورين ")
saudidevorg.configure(bg='#70a1ff')
myFont = 'arial', 20, 'bold'
bgcolor = '#70a1ff'

def raise_frame(frame):
    frame.tkraise()

fr1 = Frame(saudidevorg, bg=bgcolor, bd=3)
fr1.grid(row=1, column=0)

TopFrame = Frame(saudidevorg, bg="#70a1ff", pady=2,
                 width=400, height=100, relief=RIDGE)
TopFrame.grid(row=0, column=0)
lbtitle = Label(TopFrame, text=" Tic-Ta-Toe Project With saudidevorg ", font=(
    'arial', 18, 'bold'), bd=21, bg="#70a1ff")
lbtitle.grid(row=0, column=0)
mainframe = Frame(saudidevorg, pady=2, width=600, bg="#70a1ff",
                  height=500, relief=SOLID, bd=2)
mainframe.grid(row=1, column=0)

leftframe = Frame(mainframe, bg="#70a1ff", bd=10,  pady=2,
                  padx=10, width=500, height=500, relief=RIDGE)
leftframe.pack(side=LEFT)

rightframe = Frame(mainframe, bd=10, bg="#70a1ff", pady=2,
                   width=500, height=200, relief=RIDGE)
rightframe.pack(side=RIGHT)

toprightframe = Frame(rightframe, bd=10, bg="#70a1ff", pady=2,
                      padx=10, width=600, height=200, relief=RIDGE)
toprightframe.grid(row=0, column=0)

botrightframe = Frame(rightframe, bd=10, bg="#70a1ff", pady=2,
                      padx=10, width=400, height=200, relief=RIDGE)
botrightframe.grid(row=3, column=0)

for frame in (fr1, mainframe):
    frame.grid(row=1, column=0, sticky='news')

def raise_frame(frame):
    if len(entry_1.get()) == 0 or len(entry_2.get()) == 0:
        messagebox.showinfo("Title", "a Tk MessageBox")
         
        frame.tkraise()        
  
 
    
         



#############
# داله تمكن اللاعبين من إدخال اسمائهم في وحفظها قبل الدخول للعبه
def Playersname(): 
    name_of_user = entry_1.get()
    string_to_display = name_of_user
    var_1.set(string_to_display)
    name_of_user = entry_2.get()
    string_to_display = name_of_user
    var_2.set(string_to_display)


# def PlayerO():
#     name_of_user = entry_2.get()
#     string_to_display = name_of_user
#     var_2.set(string_to_display)
 

var_1 = StringVar()
var_2 = StringVar()

label_1 = Label(fr1, text="Enter PlayerX Name", bd=1, relief=RIDGE, pady=2, padx=2, fon=myFont)
label_2 = Label(fr1, text="Enter PlayerO Name", bd=1, relief=RIDGE, pady=2, padx=2, fon=myFont)
entry_1 = Entry(fr1, bd=3, relief=RIDGE, width=20, fon=myFont)
entry_2 = Entry(fr1, bd=3, relief=RIDGE, width=20, fon=myFont)
button_1 = Button(fr1, text="Save Players Names", bd=1, relief=RIDGE, pady=2, padx=2, fon=myFont, command=Playersname)

label_22 = Label(fr1, textvariable=var_1)
label_33 = Label(fr1, textvariable=var_2)

label_1.grid(row=0, column=0)
label_2.grid(row=1, column=0)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
button_1.grid(row=2, column=1)



    

Human = Button(saudidevorg, text='VS Human', font=myFont, padx=10,command=lambda: raise_frame(mainframe))  
bclose = Button(saudidevorg, text="Exit", font=myFont,command=saudidevorg.destroy)
Human.grid(row=2, column=0)
bclose.grid(row=3, column=0)

raise_frame(fr1)
saudidevorg.mainloop()