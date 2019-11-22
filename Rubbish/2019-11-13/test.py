from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import messagebox
from PIL import ImageTk, Image

saudidevorg = Tk() # اسم الفورم
saudidevorg.iconbitmap('8077483 (1).ico') # ايقونة الفورم

width_of_window = 880 # عرض الفورم
height_of_window = 620 # ارتفاع الفورم

#############
#توسيط الفورم على الشاشه تلقائيا
screen_width = saudidevorg.winfo_screenwidth()
screen_height = saudidevorg.winfo_screenheight()
x_coordinate = (screen_width/2) - (width_of_window/2)
y_coordinate = (screen_height/2) - (height_of_window/2)
saudidevorg.geometry("%dx%d+%d+%d" % (width_of_window,
                                      height_of_window, x_coordinate, y_coordinate))
#############
saudidevorg.title(" المبادرة السعودية للمطورين ") # اسم الفورم
saudidevorg.configure(bg='#70a1ff') # لون خلفية الفورم



# path = "small.jpg" # مسار الصوره
# img = ImageTk.PhotoImage(Image.open(path))
# panel = Label(saudidevorg, image = img, width=300)
# panel.grid(row=2, column=1, padx=10, pady=10)




# الى هنا نهاية الكود الخاص بالفورم 
#-----------------------------

lab1 = Label(saudidevorg, text="طريقة توزيع الازرار في الفورم")

lab1.grid(row=0, column=1, pady=5) # هذا ليبل وضعته في الحقل رقم 0 والعامود رقم1 

button1 = Button(saudidevorg, text="Button1- row-1, column-0", bg='blue', fg='white', font=20, width=30) # هذا زر  ويمكن التحكم بخصائصه 
# موقع الزر في الفورم -- رقم الحقل يبدا بصفر وكذلك الاعمده
button1.grid(row=1, column=0, padx=5) # هنا وضعنا الزر في الحقل رقم 1 والعامود رقم 0

button2 = Button(saudidevorg, text="Button2 row-1, column-1", bg='green', fg='white', font=20, width=30)
button2.grid(row=1, column=1, padx=5) # هنا وضعنا الزر في الحقل رقم 1 والعامود رقم1


button3 = Button(saudidevorg, text="Button3 row-1, column-2", bg='red', fg='white', font=20, width=30)
button3.grid(row=1, column=2, padx=5) # هنا وضعنا الزر في الحقل رقم 1 والعامود رقم 2


fram1 = Frame(saudidevorg, width=2000,pady=15,padx=15, bd=2,bg="yellow", relief=RIDGE)
fram1.grid(row=3, column=1, pady=20)

button4 = Button(fram1, text="Button inside Frame", bg='red', fg='white', font=20, width=30)
button4.grid(row=1, column=0, padx=5) # هنا وضعنا الزر في الحقل رقم 1 والعامود رقم 2


saudidevorg.mainloop()