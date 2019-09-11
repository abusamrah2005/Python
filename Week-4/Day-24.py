# Python Week4 Day-24
# Python Dictionaries 3

print("--- Copy a Dictionary ---\n")
# Make a copy of a Dictionary with th opy() method .
mydict = {
    "brand":"Toyota",
    "model":"Camry",
    "year":2020
}
my_car = mydict.copy()
print(my_car)

print("\n--- Copy a Dictionary ---\n")
# Another way to make a copy is to use the built-in method dict()
mydict = {
    "brand":"Toyota",
    "model":"Camry",
    "year":2020
}

MyCarInfo = dict (mydict)
print(MyCarInfo)

print("\n--- Nested Dictionaries ---\n")

My_children = {
  "first" : {
    "name" : "Ali",
    "Birth" : 2014
  },
  "second" : {
    "name" : "Saeed",
    "Birth" : 2017
  },
  "third" : {
    "name" : "Ayman",
    "Birth" : 2019
  }
}

print(My_children)
print("\n--- Nested Dictionaries ---\n")
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries
first = {
  "name" : "Ali",
  "year" : 2014
}
second = {
  "name" : "Saeed",
  "year" : 2017
}
third = {
  "name" : "Ayman",
  "year" : 2019
}

My_children = {
  "first" : first,
  "second" : second,
  "third" : third
}
print(My_children)

print("\n--- Nested Dictionaries ---\n")

my_car_info = dict(brand="Toyota", model="Camry", year=2020)

print(my_car_info)

print("\n--- End ---\n")






