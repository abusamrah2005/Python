# Python Week 3 Day-17
# Data Structures
# Python Tuples 2 
"""
Check if Item Exists To determine if a specified item is present in
 a tuple use the "in" keyword.
"""
print("Cars Brands","= ""Kia", "Nissan", "Toyota", "Bmw")
ch = input("Please Inter Car Brand : ")
Cars_Brands = ("Kia", "Nissan", "Toyota", "Bmw")
if "Kia" in ch:
    print("yes, {} in Cars Brands".format(ch))
else:
    print("No, {} Not In Cars Brands".format(ch))
print("\n-----------------------------------------\n")

# Repeat Item
# To repeat an item in a tuple, use the * operator.
print("Repeat item")
thistuple = ("Python",)*3
print(thistuple)
print("\n-----------------------------------------\n")
# + Operator in Tuple
# To add 2 tuples or more into one tuple.

print(""" 'add 2 tuples'
Cars_Brands1 = ("Kia", "Nissan", "Toyota", "Bmw")
Cars_Brands2 = ("Chevrolet", "Ford")
mycars = Cars_Brands1 + Cars_Brands2 
""")
Cars_Brands1 = ("Kia", "Nissan", "Toyota", "Bmw")
Cars_Brands2 = ("Chevrolet", "Ford")
mycars = Cars_Brands1 + Cars_Brands2 
print("Result = ", mycars)
print("\n-----------------------------------------\n")

# Print the number of items in the tuple

Cars_Number = ("Kia", "Nissan", "Toyota", "Bmw")
print("number of items Is : ",len(Cars_Number))
print("\n-----------------------------------------\n")
# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.

print(
"""
method We Use : cartuple = tuple(("Chevrolet", "Ford"))
"""
)
cartuple = tuple(("Chevrolet", "Ford"))
print(cartuple)
print("\n-----------------------------------------\n")

# Convert a list into a tuple

mylist = [1, 2, 3, "A", "B", "C"]
Convert = tuple(mylist)
print(Convert)