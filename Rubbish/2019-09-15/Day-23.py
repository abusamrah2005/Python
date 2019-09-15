# Python Week4 Day-23
# القواميس )المعاجم( في لغة البايثون
# Python Dictionaries 2

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword.

print("-------Check if Key Exists-----------\n")
mydict = {
    "brand":"Toyota",
    "model":"Camry",
    "year":2020
}

if "model" in mydict:
    print("Yes, model  in the dictionary")

print("---------------------------------")
print("------Dictionary Length-----------")

# Dictionary Length
mydict1 = {
    "brand":"Toyota",
    "model":"Camry",
    "year":2020
}
print(" number of items in the dictionary is : ",len( mydict1))
print("---------------------------------")
print("----------Adding Items-----------")
# Adding an item to the dictionary is done by using a new index key and assigning a value to it.
mydict2 = {
    "brand":"Toyota",
    "model":"Camry",
    "year":2020
}
mydict2["color"] = "Red"
print(mydict2)
print("---------------------------------")
print("---------Removing Items----------")
# The pop() method removes the item with the specified key name.

mydict3 = {
    "brand":"Toyota",
    "model":"Camry",
    "year":2020
}

mydict.pop("year")
print(mydict3)
print("---------------------------------")
print("-----------popitem()-------------")
# The popitem() method removes the last inserted item.
mydict4 = {
    "brand":"Toyota",
    "model":"Camry",
    "year":2020
}

mydict4.popitem()
print(mydict4)
print("---------------------------------")
print("---------del keyword-------------")
# The del keyword removes the item with the specified key name.

mydict5 = {
    "brand":"Toyota",
    "model":"Camry",
    "year":2020
}
del mydict5["brand"]
print(mydict5)
print("---------------------------------")
print("---------del keyword-------------")
# The del keyword can also delete the dictionary completely.

mydict6 = {
    "brand":"Toyota",
    "model":"Camry",
    "year":2020
}
try: # to skip the error and show you Message
    del mydict6

except NameError as err:
    print(mydict6) #this will cause an error because "thisdict" no longer exists.
else:
    print("ther is no Dictionary")

print("---------------------------------")
print("---------clear()-------------")

mydict7 = {
    "brand":"Toyota",
    "model":"Camry",
    "year":2020
}
mydict7.clear()
print(mydict7)