"""
تحدي الأسبوع )يتم حله ورفعه على Github )
أولًا:
قم بإنشاء قائمة وطبّق عليها ٤ دوال مما تعلمته خلال هذا الأسبوع

ثانيًا:
قم بكتابة نص برمجي ) كود ( لتتأكد عن طريقه من وجود العنصر python في
tuple = (“java", “python", “swift")
انتظرنا في
"""
my_list = ["France", "German", "Japan", "English", "Russian", "Arabic"]
print("Sorting a List of Strings\n")
print(my_list)
my_list.sort()
print("\nAfter sorting\n")
print(my_list)
print("-------------------------------------\n")
print("Add new language")
my_list.append(input("Please Insert language : "))
print("The New language Added to The List")
print(my_list)
print("-------------------------------------\n")
print("Remove language")
rem = input("Please Select language to Remove : ")
if rem in my_list:
    my_list.remove(rem)
    print("OK, The {} language Has deleted From The List".format(rem))
else:
    print("Sorry, The language {}  is Not in The List".format(rem))
print(my_list)
print("\n-------------------------------------\n")
print("Clear All Items")
my_list.clear()
print(my_list)
print("\n-------------------------------------\n")
tuple = ("java", "python", "swift")
ser = input(" Please Insert Item Name : ")
if ser in tuple:
    print(" {} is in The Tuple  ".format(ser))
else:
    print(" {} is Not in The Tuple".format(ser))
