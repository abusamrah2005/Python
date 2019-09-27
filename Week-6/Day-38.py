# Paython Week-6 Day-38
# Python Arrays 2

print(" Looping Array Elementsv ")

cars = ["Ford", "Volvo", "BMW"]

for x in cars:
  print(x)

print("\n Adding Array Elements ")

cars1 = ["Ford", "Volvo", "BMW"]

cars1.append("Toyota")

print(cars1)

print("\n Delete the Therd element of the cars array  ")

cars2 = ["Ford", "Volvo", "BMW"]

cars2.pop(2)

print(cars2)

print(" \n Delete the element that has the value 'BMW' ")
cars3 = ["Ford", "Volvo", "BMW"]

cars3.remove("BMW")

print(cars3)