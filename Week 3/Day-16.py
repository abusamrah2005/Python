
# Python Week 3  Day-16
# الصفوف )الأزواج المرتبة( في لغة البايثون
# Python Tuples

mytuple = ("Python", "Java", "C++", "C#")
print(mytuple)

print("--------------------------------\n")

# في المثال التالي قمنا بتعريف tuple فارغ ، لا يحتوي على أي عنصر.
# An empty tuple in Python.

EmptyTuple = ()

print(EmptyTuple)

print("--------------------------------\n")

# في المثال التالي قمنا بتعريف tuple يحتوي على عنصر واحد فقط.
#
tupleitem = ("Python",)
print(tupleitem)

print("--------------------------------\n")

# في المثال التالي قمنا بتعريف tuple يحتوي على أعداد صحيحة وعشرية
# هنا لا حاجة لوضع فاصلة , إضافية بعد آخر قيمة كما في المثال السابق


num_tuple = (2, 3, 1.5, 3.7)
print(num_tuple)

print("--------------------------------\n")

# The data inside a tuple can be of one or more data types.
"""
في المثال التالي قمنا بتعريف tuple يحتوي على عدة أنواع
من أنواع البيانات: أعداد صحيحة، أعداد عشرية، ونصوص.
"""
data_types_tuple = ("Samsung", 2, "Apple", 2.3)
print(data_types_tuple)

print("--------------------------------\n")

# للوصول لأي عنصر في tuplee عليك استخدام رقم ال index الخاص بالعنصر، باستخدام الأقواس المربعة []
# You can access tuple items by referring to the index number, inside square brackets [].
"""
print(tuple_items[1])
print(tuple_items[2])
print(tuple_items[3])
"""

tuple_items = ("Python", "Java", "C++", "C#")

print( " 0- Python", " 1- Java", " 2- C++", " 3- C#")

# Example
print("index 0 = ",tuple_items[0])
print("index 1 = ",tuple_items[1])
print("index 2 = ",tuple_items[2])
print("index 3 = ",tuple_items[3])


print("--------------------------------\n")

# Once a tuple is created, you cannot change its values. Tuples are unchangeable.
# في ال tuple لا يمكنك تغيير القيم التي تسندها إليها أثناء إنشائها، فهي غير قابلة للتغير أو التعديل عليها.
# في ال tuple القيم غير قابلة للتغيير أو التعديل عليها.

print("--------------------------------\n")

"""
هنا قمنا بتعريف tuple تحتوي على نصوص
ثم قمنا بطباعة جميع القيم باستخدام الحلقة
You can loop through the tuple items by using a for loop.
"""

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
for basket in thistuple:
    print(basket)

print("--------------------------------\n")

"""
تقسيم ال tuple إلى أجزاء / تجزئة ال tuple
إذا أردنا عرض أو طباعة جزء من عناصر ال tuple نقوم بعرض العناصر كما في القوائم عن طريق رقم ال index

Divide the tuple into parts / fragment the tuple
If we want to display or print part of the items tuple we display the items as in the menus via Index

"""

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(" 0- apple", " 1- banana", " 2- cherry", " 3- orange", " 4- kiwi", " 5- melon", " 6- mango")

# Example
print(thistuple[0:2])
print(thistuple[2:4])
print(thistuple[4:6])
print(thistuple[3:])
print(thistuple[1:5])
print("\n--------------------------------\n")
print("--------------------------------\n")
print("--------------------------------\n")