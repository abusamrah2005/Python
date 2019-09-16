# Python Week-5 Day-27


"""Conditional Statements
Python If … Else"""

x = 30
y = 20

# Conditional Statements . Python If … Else
x = 30
y = 20
if x > y:
    print("{} is greater than {}".format(x, y))

print("\n-_-_-_-_-_-_-_-_\n")

a = 50
b = 50
if a> b:
    print("{} is greater than {}".format(a, b))
elif a == b:

    print("{} And {} Are equal ".format(a, b))

    print("{} And {} Are equal ".format(a, b))

print("\n-_-_-_-_-_-_-_-_\n")
k = 500
p = 50
if p> k:
    print("{} is greater than {}".format(k, p))
elif k == p:
    print("{} And {} Are equal ".format(k, p))
else:
    print("{} is greater than {} ".format(k, p))

print("\n-_-_-_-_-_-_-_-_\n")
w = 2200
q = 1000
# One line if statement
if w > q:print("{} is greater than {}".format(w, q))


print("\n-_-_-_-_-_-_-_-_\n")
# One line if else statement
SS = 8
BB = 10
print("ss") if SS > BB else print("BB")

print("\n-_-_-_-_-_-_-_-_\n")
# One line if else statement, with 3 conditions
xx = 300
yy = 300
print("xx") if xx > yy else print("'='") if xx == yy else print("yy")

print("\n-_-_-_-_-_-_-_-_\n")
# Test if a is greater than b, AND if c is greater than a
mm = 50
nn = 20
hh = 100
if mm > nn and hh > nn:
    print(" 1- Both conditions are true")

# The or keyword is a logical operator, and is used to combine conditional statements
aa = 35
dd = 15
vv = 45

if a > dd or aa > vv:
    print(" 2- One of the conditions is true")

print("\n-_-_-_-_-_-_-_-_\n")

print("default user name is ( admin )")
name = "admin"
while True:
    user = input("Enter user name : ")
    if name == user:
        print("Hi admin, you are in control panel")
        break
    else:
        print ("you are not authorized to view this page. Try Agine : ")
        

