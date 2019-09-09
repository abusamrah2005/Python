# Python Week4 Day22
# القواميس )المعاجم( في لغة البايثون
# Python Dictionaries
print("-------- Empty dictionary -----------\n")
# Example
# an Empty dictionary.
myDict = {}
print (myDict)
print("\n------ {keys : values} ------------\n")
# dictionary name = {keys : values}dictionary name = {keys : values}
# Example
Mydict0 = {
  "brand": "Chevrolet",
  "model": "Caprice",
  "year": 1990
}
print(Mydict0)
print("\n--------- Accessing Items ------------\n")
# You can access the items of a dictionary by referring to its key name,
# inside square brackets [].
# Example
# Get the value of the "model" key.
Mydict1 = {
  "brand": "Chevrolet",
  "model": "Caprice",
  "year": 1990
}
x = Mydict1["model"]
print(x)
# There is also a method called get() that will give you the same result.
Mydict1 = {
  "brand": "Chevrolet",
  "model": "Caprice",
  "year": 1990
}
x = Mydict1.get("model")
print(x)

print("\n--------- Change Values ------------\n")
Mydict2 = {
  "brand": "Chevrolet",
  "model": "Caprice",
  "year": 1990
}
Mydict2["year"] = 1989
print(Mydict2)

print("\n------ Loop Through a Dictionary ---------\n")
# You can loop through a dictionary by using a for loop.
Mydict3 = {
  "brand": "Chevrolet",
  "model": "Caprice",
  "year": 1990
}

for key in Mydict3:
    print(" Key :", key)
print("____________________")
# Print all values in the dictionary, one by one    
Mydict4 = {
  "brand": "Chevrolet",
  "model": "Caprice",
  "year": 1990
}

for x in Mydict4:
    print(" Item : ", Mydict4[x])
print("____________________")
# You can also use the values() function to return values of a dictionary. 
Mydict5 = {
  "brand": "Chevrolet",
  "model": "Caprice",
  "year": 1990
}

for x in Mydict5.values():
    print(" value : ", x)

print("\n------------ items() -------------\n")
# Loop through both keys and values, by using the items() function.
Mydict6 = {
  "brand": "Chevrolet",
  "model": "Caprice",
  "year": 1990
}

for x, y in Mydict6.items():
    print(x, "➢",  y)  

# You can use the items() function to display all existing elements without using the loop for

Mydict7 = {
  "brand": "Chevrolet",
  "model": "Caprice",
  "year": 1990
}

print(Mydict7.items())  


print("\n------------ Finish -------------\n")

