# المجموعات في لغة البايثون
# Python Week4 Day-20
# Python Sets
# A set is a collection which is unordered and unindexed.
# In Python sets are written with curly brackets {}.

print("Example: Empty Set.")
myset = {}
print(myset)
print("---------------------")
print("Note: Sets are unordered, so you cannot be sure in which order the items will appear.")
print("---------------------")

"""
أردنا توضيح أن المجموعات لا تحتوي على قيم مكررة، قيمها تكون دائما فريدة.
ولا ننسى أيضا أنها غير مرتبة لذلك ظهرت النتيجة بهذه الصورة.
myset1 = {"Mohammed", "Mohammed", "1", "1"}
"""
myset1 = {"Mohammed", "Mohammed", "1", "1"}
print(myset1)
print("---------------------")
"""
But you can loop through the set items using a for loop, 
or ask if a specified value is present in a set, 
by using the in keyword.
"""
myset2 = {"Python", "JavaScript", "Html", "Css"}
for set in myset2:
    print(set)
print("---------------------")
# Example: Check if "banana" is present in the set.
myset3 = {"Python", "JavaScript", "Html", "Css"}
print("Python" in myset3)
print("Java" in myset3)
print("---------------------")
# To add one item to a set use the add() method.

myset4 = {"Python", "JavaScript", "Html", "Css"}
myset4.add("Java")
print(myset4)
print("---------------------")
# To add more than one item to a set use the update() method.
myset5 = {"Python"}

myset5.update(["Html", "Css"])
print(myset5)
print("---------------------")



