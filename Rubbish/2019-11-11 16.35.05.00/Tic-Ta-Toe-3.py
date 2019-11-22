# Tic-Ta-Toe
from tkinter import *
from tkinter.messagebox import showinfo



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



#############
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

label_1 = Label(fr1, text="Enter nameX")
label_2 = Label(fr1, text="Enter nameO")
entry_1 = Entry(fr1)
entry_2 = Entry(fr1)
button_1 = Button(fr1, text="Save Player X Name", command=Playersname)
button_2 = Button(fr1, text="Save Player O Name", command=PlayerO)
label_22 = Label(fr1, textvariable=var_1)
label_33 = Label(fr1, textvariable=var_2)

label_1.grid(row=0, column=0)
label_2.grid(row=1, column=0)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
button_1.grid(row=0, column=2)
button_2.grid(row=1, column=2)


Human = Button(saudidevorg, text='VS Human', font=myFont, padx=10,command=lambda: raise_frame(mainframe))  
bclose = Button(saudidevorg, text="Exit", font=myFont,command=saudidevorg.destroy)
Human.grid(row=2, column=0)
bclose.grid(row=3, column=0)
    
###############
# txtnameX = Entry(fr1, font=myFont, bg='#f1f2f6',
#                    fg="black", bd=2, width=15, justify=LEFT)
# txtnameX.grid(row=2, column=1)                  
# txtnameO = Entry(fr1, font=myFont, bg='#f1f2f6',
#                    fg="black", bd=2, width=15, justify=LEFT)
# txtnameO.grid(row=2, column=1)
################


PlayerX = IntVar()
PlayerO = IntVar()

PlayerX.set(0)
PlayerO.set(0)

buttons = StringVar()
click = True

def Buttonsdisabled(): # دالة تعطيل الازرار عند فوز احد الطرفين
    b1["state"] = "disabled"
    b2["state"] = "disabled"
    b3["state"] = "disabled"
    b4["state"] = "disabled"
    b5["state"] = "disabled"
    b6["state"] = "disabled"
    b7["state"] = "disabled"
    b8["state"] = "disabled"
    b9["state"] = "disabled"

def Buttonsnormal(): # Reset او New Game دالة تفعيل الازرار بعد الضغط على 
    b1["state"] = "normal"
    b2["state"] = "normal"
    b3["state"] = "normal"
    b4["state"] = "normal"
    b5["state"] = "normal"
    b6["state"] = "normal"
    b7["state"] = "normal"
    b8["state"] = "normal"
    b9["state"] = "normal"

def checker(buttons): # دالة التحقق من اللاعب الذي ضغط على الزر وتسمية الزر
    global click
    if buttons['text'] == '' and click == True:
        buttons["text"] = "X"
        click = False
        result()
    elif buttons['text'] == '' and click == False:
        buttons["text"] = "O"
        click = True
        result()

def reset(): # مسح نص جميع الازرار وإعادة تفعيلها
    b1['text'] = ""
    b2['text'] = ""
    b3['text'] = ""
    b4['text'] = ""
    b5['text'] = ""
    b6['text'] = ""
    b7['text'] = ""
    b8['text'] = ""
    b9['text'] = ""
    Buttonsnormal()

    b1.configure(background="#ced6e0")
    b2.configure(background="#ced6e0")
    b3.configure(background="#ced6e0")
    b4.configure(background="#ced6e0")
    b5.configure(background="#ced6e0")
    b6.configure(background="#ced6e0")
    b7.configure(background="#ced6e0")
    b8.configure(background="#ced6e0")
    b9.configure(background="#ced6e0")

def NewGame(): # تصفير نتيجة اللاعبين وبدء لعبة جديد وتفعيل الازرار
    PlayerX.set(0)
    PlayerO.set(0)
    b1['text'] = ""
    b2['text'] = ""
    b3['text'] = ""
    b4['text'] = ""
    b5['text'] = ""
    b6['text'] = ""
    b7['text'] = ""
    b8['text'] = ""
    b9['text'] = ""
    Buttonsnormal()

    b1.configure(background="#ced6e0")
    b2.configure(background="#ced6e0")
    b3.configure(background="#ced6e0")
    b4.configure(background="#ced6e0")
    b5.configure(background="#ced6e0")
    b6.configure(background="#ced6e0")
    b7.configure(background="#ced6e0")
    b8.configure(background="#ced6e0")
    b9.configure(background="#ced6e0")


'''  X او  O عند تطابق نص الازرار 
 Reset او New Game ستظهر رسالة بفوز اللاعب ويتم تعطيل الازرار حتى يتم الضغط على
 تحقق من إشارة 3 ازرار متتاليه
'''
def result():  
    if (b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X"):
        b1.configure(background="#eccc68")
        b2.configure(background="#eccc68")
        b3.configure(background="#eccc68")
        result = int(PlayerX.get())
        score = (result + 1)
        PlayerX.set(score)
        showinfo("Winner Player X",
                 "You Won A gmae ,  Player O Lose\n Press Reset To Try Agine")
        Buttonsdisabled()

    elif (b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X"):
        b4.configure(background="#eccc68")
        b5.configure(background="#eccc68")
        b6.configure(background="#eccc68")
        result = int(PlayerX.get())
        score = (result + 1)
        PlayerX.set(score)
        showinfo("Winner Player X",
                 "You Won A gmae ,  Player O Lose\n Press Reset To Try Agine")
        Buttonsdisabled()

    elif (b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X"):
        b7.configure(background="#eccc68")
        b8.configure(background="#eccc68")
        b9.configure(background="#eccc68")
        result = int(PlayerX.get())
        score = (result + 1)
        PlayerX.set(score)
        showinfo("Winner Player X",
                 "You Won A gmae ,  Player O Lose\n Press Reset To Try Agine")
        Buttonsdisabled()

    elif (b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O"):
        b1.configure(background="#eccc68")
        b2.configure(background="#eccc68")
        b3.configure(background="#eccc68")
        result = int(PlayerO.get())
        score = (result + 1)
        PlayerO.set(score)
        showinfo("Winner Player O",
                 "You Won A gmae ,  Player X Lose\n Press Reset To Try Agine")
        Buttonsdisabled()

    elif (b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O"):
        b4.configure(background="#eccc68")
        b5.configure(background="#eccc68")
        b6.configure(background="#eccc68")
        result = int(PlayerO.get())
        score = (result + 1)
        PlayerO.set(score)
        showinfo("Winner Player O",
                 "You Won A gmae ,  Player X Lose\n Press Reset To Try Agine")
        Buttonsdisabled()

    elif (b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O"):
        b7.configure(background="#eccc68")
        b8.configure(background="#eccc68")
        b9.configure(background="#eccc68")
        result = int(PlayerO.get())
        score = (result + 1)
        PlayerO.set(score)
        showinfo("Winner Player O",
                 "You Won A gmae ,  Player X Lose\n Press Reset To Try Agine")
        Buttonsdisabled()

    elif (b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X"):
        b3.configure(background="#eccc68")
        b5.configure(background="#eccc68")
        b7.configure(background="#eccc68")
        result = int(PlayerX.get())
        score = (result + 1)
        PlayerX.set(score)
        showinfo("Winner Player X",
                 "You Won A gmae ,  Player O Lose\n Press Reset To Try Agine")
        Buttonsdisabled()

    elif (b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X"):
        b1.configure(background="#eccc68")
        b5.configure(background="#eccc68")
        b9.configure(background="#eccc68")
        result = int(PlayerX.get())
        score = (result + 1)
        PlayerX.set(score)
        showinfo("Winner Player X",
                 "You Won A gmae ,  Player O Lose\n Press Reset To Try Agine")
        Buttonsdisabled()

    elif (b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O"):
        b4.configure(background="#eccc68")
        b5.configure(background="#eccc68")
        b6.configure(background="#eccc68")
        result = int(PlayerO.get())
        score = (result + 1)
        PlayerO.set(score)
        showinfo("Winner Player O",
                 "You Won A gmae ,  Player X Lose\n Press Reset To Try Agine")
        Buttonsdisabled()

    elif (b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O"):
        b7.configure(background="#eccc68")
        b8.configure(background="#eccc68")
        b9.configure(background="#eccc68")
        result = int(PlayerO.get())
        score = (result + 1)
        PlayerO.set(score)
        showinfo("Winner Player O",
                 "You Won A gmae ,  Player X Lose\n Press Reset To Try Agine")
        Buttonsdisabled()

    elif (b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O"):
        b3.configure(background="#eccc68")
        b5.configure(background="#eccc68")
        b7.configure(background="#eccc68")
        result = int(PlayerO.get())
        score = (result + 1)
        PlayerO.set(score)
        showinfo("Winner Player O",
                 "You Won A gmae ,  Player X Lose\n Press Reset To Try Agine")
        Buttonsdisabled()

    elif (b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O"):
        b1.configure(background="#eccc68")
        b5.configure(background="#eccc68")
        b9.configure(background="#eccc68")
        result = int(PlayerO.get())
        score = (result + 1)
        PlayerO.set(score)
        showinfo("Winner Player O",
                 "You Won A gmae ,  Player X Lose\n Press Reset To Try Agine")
        Buttonsdisabled()

    elif (b1["text"] == "O" and b5["text"] == "O" and b7["text"] == "O"):
        b1.configure(background="#eccc68")
        b4.configure(background="#eccc68")
        b7.configure(background="#eccc68")
        result = int(PlayerO.get())
        score = (result + 1)
        PlayerO.set(score)
        showinfo("Winner Player O",
                 "You Won A gmae ,  Player X Lose\n Press Reset To Try Agine")
        Buttonsdisabled()

    elif (b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O"):
        b2.configure(background="#eccc68")
        b5.configure(background="#eccc68")
        b8.configure(background="#eccc68")
        result = int(PlayerO.get())
        score = (result + 1)
        PlayerO.set(score)
        showinfo("Winner Player O",
                 "You Won A gmae ,  Player X Lose\n Press Reset To Try Agine")
        Buttonsdisabled()

    elif (b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O"):
        b3.configure(background="#eccc68")
        b6.configure(background="#eccc68")
        b9.configure(background="#eccc68")
        result = int(PlayerO.get())
        score = (result + 1)
        PlayerO.set(score)
        showinfo("Winner Player O",
                 "You Won A gmae ,  Player x Lose\n Press Reset To Try Agine")
        Buttonsdisabled()

    elif (b1["text"] == "ْX" and b4["text"] == "X" and b7["text"] == "X"):
        b1.configure(background="#eccc68")
        b4.configure(background="#eccc68")
        b7.configure(background="#eccc68")
        result = int(PlayerX.get())
        score = (result + 1)
        PlayerX.set(score)
        showinfo("Winner Player X",
                 "You Won A gmae ,  Player O Lose\n Press Reset To Try Agine")
        Buttonsdisabled()

    elif (b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X"):
        b2.configure(background="#eccc68")
        b5.configure(background="#eccc68")
        b8.configure(background="#eccc68")
        result = int(PlayerX.get())
        score = (result + 1)
        PlayerX.set(score)
        showinfo("Winner Player X",
                 "You Won A gmae ,  Player O Lose\n Press Reset To Try Agine")
        Buttonsdisabled()

    elif (b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X"):
        b3.configure(background="#eccc68")
        b6.configure(background="#eccc68")
        b9.configure(background="#eccc68")
        result = int(PlayerX.get())
        score = (result + 1)
        PlayerX.set(score)
        showinfo("Winner Player X",
                 "You Won A gmae ,  Player O Lose\n Press Reset To Try Agine")
        Buttonsdisabled()

    elif (b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O"):
        b3.configure(background="#eccc68")
        b6.configure(background="#eccc68")
        b9.configure(background="#eccc68")
        result = int(PlayerO.get())
        score = (result + 1)
        PlayerO.set(score)
        showinfo("Winner Player O",
                 "You Won A gmae ,  Player X Lose\n Press Reset To Try Agine")
        Buttonsdisabled()

    elif (b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O"):
        b1.configure(background="#eccc68")
        b4.configure(background="#eccc68")
        b7.configure(background="#eccc68")
        result = int(PlayerO.get())
        score = (result + 1)
        PlayerO.set(score)
        showinfo("Winner Player O",
                 "You Won A gmae ,  Player X Lose\n Press Reset To Try Agine")
        Buttonsdisabled()

    elif (b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X"):
        b1.configure(background="#eccc68")
        b4.configure(background="#eccc68")
        b7.configure(background="#eccc68")
        result = int(PlayerX.get())
        score = (result + 1)
        PlayerX.set(score)
        showinfo("Winner Player X",
                 "You Won A gmae ,  Player O Lose\n Press Reset To Try Agine")
        Buttonsdisabled()





lablplayerX = Label(toprightframe, textvariable=var_1,
                    font=myFont, pady=2, padx=2, bg="#70a1ff")
lablplayerX.grid(row=0, column=0, sticky=W)

txtplayerX = Entry(toprightframe, font=myFont, bg='#f1f2f6',
                   fg="black", bd=2, textvariable=PlayerX, width=15, justify=LEFT).grid(row=0, column=1)

lablplayerO = Label(toprightframe, textvariable=var_2,
                    font=myFont, pady=2, padx=2, bg="#70a1ff").grid(row=1, column=0, sticky=W)
txtplayerO = Entry(toprightframe, font=myFont, bg='#f1f2f6',
                   fg="black", bd=2, textvariable=PlayerO, width=15, justify=LEFT).grid(row=1, column=1)

reset = Button(botrightframe,  text="Reset", font=myFont,
               width=20,  height=1, bg='#1e90ff', command=reset)
reset.grid(row=1, column=0, padx=6, pady=10)

new_game = Button(botrightframe,  text="New Game", font=myFont,
                  width=20,  height=1, bg='#1e90ff', command=NewGame)
new_game.grid(row=2, column=0, padx=6, pady=10)

b1 = Button(leftframe,  text="",  width=15,  height=8, bg='#ced6e0',
            command=lambda: checker(b1))
b1.grid(row=1, column=0, sticky=S+N+E+W)

b2 = Button(leftframe,  text="",  width=15,  height=8, bg='#ced6e0',
            command=lambda: checker(b2))
b2.grid(row=1, column=1, sticky=S+N+E+W)

b3 = Button(leftframe,  text="",  width=15,  height=8, bg='#ced6e0',
            command=lambda: checker(b3))
b3.grid(row=1, column=2, sticky=S+N+E+W)

b4 = Button(leftframe,  text="",  width=15,  height=8, bg='#ced6e0',
            command=lambda: checker(b4))
b4.grid(row=2, column=0, sticky=S+N+E+W)

b5 = Button(leftframe,  text="",  width=15,  height=8, bg='#ced6e0',
            command=lambda: checker(b5))
b5.grid(row=2, column=1, sticky=S+N+E+W)

b6 = Button(leftframe,  text="",  width=15,  height=8, bg='#ced6e0',
            command=lambda: checker(b6))
b6.grid(row=2, column=2, sticky=S+N+E+W)

b7 = Button(leftframe,  text="",  width=15,  height=8, bg='#ced6e0',
            command=lambda: checker(b7))
b7.grid(row=3, column=0, sticky=S+N+E+W)

b8 = Button(leftframe,  text="",  width=15,  height=8, bg='#ced6e0',
            command=lambda: checker(b8))
b8.grid(row=3, column=1, sticky=S+N+E+W)

b9 = Button(leftframe,  text="",  width=15,  height=8, bg='#ced6e0',
            command=lambda: checker(b9))
b9.grid(row=3, column=2, sticky=S+N+E+W)


raise_frame(fr1)
saudidevorg.mainloop()
