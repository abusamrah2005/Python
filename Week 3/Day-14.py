"""

القوائم في لغة البايثون
Python Lists 2
"""
# Data Structures - هياكل البيانات

Devices = ["Apple", "Samsung", "Huawei", "Nokia"]
print(" 0 = Apple\n", "1 = Samsung\n", "2 = Huawei\n", "3 = Nokia\n")
# لكي نقوم بطباعة جزء من عناصر هذه القائمة نضع رقم الاندكس للعناصر

print("""print(Devices[0:])
print(Devices[0:3])
print(Devices[2:])
print(Devices[3])\n""")

print(Devices[0:]) # print all indexes
print(Devices[0:3]) # print from index 0 to index 3
print(Devices[2:]) # print from index 2 to End
print(Devices[3]) # print index 3 Only


print("-------------------------------------")


# التحقق من وجود عنصر في القائمة مع السماح للمستخدم بإدخال القيمه
# Checks for an item in the list and allows the user to enter the value
# To determine if a specified item is present in a list use the in keyword.



Devices = ["Apple", "Samsung", "Huawei", "Nokia"]

userinput = input("Enter Device name : ")

if userinput in Devices:
    print("Yes, The Device {} is In Devices List. ".format(userinput))
else:
    print("no, The Device {} is not in Devices List.".format(userinput))

print("-------------------------------------")


# لتكرار قيمة معينة نستخدم العامل *
# Repeat Item in List
# To repeat an item in a list, use the * operator.

List = ["Python"]*5

print(List)

print("-------------------------------------")
# يُستخدم هذا العامل + لدمج أكثر من قائمة في قائمة واحدة.
# To add 2 lists or more into one list.

List1 = ["Python", "Java"]
List2 = ["C++", "C#"]
List3 = List1 + List2

print(List3)

print("-------------------------------------")
# بتطبيق مثال لدمج قائمتين إحداهما تحتوي على أعداد عشرية والأخرى أعداد صحيحة.
# Applies an example to merge two lists, one containing decimal numbers and the other integers.

integ = [2,3,4,5,6]
decim = [1.5,2.3,3.7,8.1]
merge = integ + decim

print(merge)

