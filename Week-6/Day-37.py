# Paython Week-6 Day-37 
# Python Arrays

print("Arrays are used to store multiple values in one single variable\n")
cars = ["Ford", "Volvo", "BMW"]
print(cars)
print("-----")
# You refer to an array element by referring to the index number.
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
y = cars[1]
z = cars[2]
print(x)
print(y)
print(z)

print("----")

# Modify the value of the first array item
cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)

print("----")
# Return the number of elements in the cars array
cars1 = ["Ford", "Volvo", "BMW"]

x = len(cars1)

print("number of elements in the cars is:", x)
