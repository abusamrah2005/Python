
"""
القوائم في لغة البايثون
Python Lists
"""

My_List = [1.5, 2.1, 5.4, 4.9, 6.3]

print(My_List)


print("----------------------------------")


"""
You access the list items by referring to the index number.
Example
Print the second item of the list
للوصول لأي عنصر في القائمة عليك استخدام رقم ال index الخاص بالعنصر الذي تريد
"""
Devices = ["Apple", "Samsung", "Huawei", "Nokia"]
Devices1 = "Apple, Samsung, Huawei, Nokia"
print(Devices1)
print("0 = Apple, 1 = Samsung, 2 = Huawei, 3 = Nokia")
print("When choosing  2 the resulte is = ",Devices[2])
print("When choosing  0 the resulte is = ",Devices[0])
print("When choosing  1 the resulte is = ",Devices[1])
print("When choosing  3 the resulte is = ",Devices[3])


print("----------------------------------")
"""
عرض جميع القيم في القائمة
Loop Through a List
"""

print("All Items In My List : ")

Devices = ["Apple", "Samsung", "Huawei", "Nokia"]
for x in Devices:
  
    print (x)

    print("------")
print("----------------------------------")

"""
تغيير قيمة العنصر
Change Item Value
"""
print(Devices1)
Devices[3] = "blackberry"
print(Devices)
print("we change nokia with blackberry")


print("----------------------------------")


"""
تُستخدم del لحذف القائمة كاملة من الذاكرة أو لحذف عنصر محدد فيها.
The del keyword removes the specified index.

 The del keyword can also delete the list completely.
 عند حذفك لعنصر ما في القائمة بواسطة del فإن العناصر ستترتب من جديد في بايثون،
وتتحدث أرقام ال index تلقائيا لكل عنصر.

"""

del Devices[3]
print(Devices)
print("We Delete Index No: 3 (blackberry)")

print(" To delete all Items In My list we usr (del (ListName))")
