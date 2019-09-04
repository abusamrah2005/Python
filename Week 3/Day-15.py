
# Week 3 Day-15
# Data Structures - هياكل البيانات
# دوال القوائم في لغة البايثون
# Python Lists 3

"""
استخدم الدالة len() لمعرفة عدد عناصر القائمة، فهي تقوم بترجيع عدد صحيح وهو عدد العناصر.

To determine how many items a list has, use the len() method.
"""


cars =  ["Toyota", "Benz", "Ford", "Nissan"]

print(cars)

print(len(cars))
print("اظهرنا عدد العناصر في القائمه")
print("----------------------------------")

# استخدم الدالة append() إذا أردت إضافة عنصر جديد في آخر القائمة
# To add an item to the end of the list, use the append() method.

cars1 = ["Toyota", "Benz", "Ford", "Nissan"]

print(cars1)
print(" append إضافة عنصر للقائمه ")
cars1.append("BMW")
print(cars1)
print("تم إضافة عنصر جديد")
print("----------------------------------")

# إضافة عنصر جديد في مكان محدد في القائمة
# To add an item at the specified index, use the insert() method.

cars2 = ["Toyota", "Benz", "Ford", "Nissan"]

print(" Add a new item to the list by specifying the index number in the list --  إضافة عنصر للقائمه بتحديد موقعه في القائمه ")
cars2.insert(1,"KIA")
print(cars2)
print("تم إضافة عنصر في مكاتن محدد اخترناه")

print("----------------------------------")

# حذف عنصر من القائمة هناك . دالتين لحذف العنصر من القائمة
# There are several methods to remove items from a list.

# الدالة الأولى هي remove() تقوم بحذف عنصر محدد في القائمة
# The remove() method removes the specified item.

cars3 = ["Toyota", "Benz", "Ford", "Nissan"]

print("remove() الحذف بواسطة")
cars3.remove("Toyota")
print(cars3)
print("تم حذف عنصر")



# دالة الحذف الثانية هي pop() تقوم بحذف عنصر محدد في القائمة
# تقوم بحذف العنصر لكن عن طريق استدعاء رقم ال index لهذا العنصر
# The pop() method removes the specified index.
# (or the last item if index is not specified).
cars4 = ["Toyota", "Benz", "Ford", "Nissan"]

print(" الحذف بواسطة   بدون تحديد رقم العنصرpop()")
cars4.pop()
print("list now : ", cars4)

print(" الحذف بواسطة ونختار رقم العنصرpop(1)")
cars4.pop(0)
print("list now : ", cars4)

print("----------------------------------")

# تُستخدم دالة clear() لحذف جميع العناصر في القائمة.
# The clear() method empties the list.
cars5 = ["Toyota", "Benz", "Ford", "Nissan"]
cars5.clear()
print("list now : ",cars5)
print("تم حذف كل محتوايات القائمه")

print("----------------------------------")

# نسخ القائمة
# Copy a List


cars6 = list (("Toyota", "Benz", "Ford", "Nissan","Benz"))
print(cars6)
print("تم نسخ العناصر الى قائمه جديده وتم طباعة هذه القائمه ")

print("----------------------------------")

cars7 = ["Toyota", "Benz", "Ford", "Nissan","Benz"]

print(cars7)
print("count() لمعرفة عدد العناصر في القائمه مع إعطائه قيمة العنصر لمعرفة العدد")
print ("cars6.count('Benz') مثال")
cars6.count("Benz")
print ("Count for Benz : ", cars7.count("Benz"))
