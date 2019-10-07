# Python Week-8 Day-49
# Python Scope 2
# The function will print the local x, and then the code will print the global x.
num1 = 300

def nums():
    num1 = 200
    print(num1)

nums()
print(num1)
print("\n-----")
print(" variable = 50")
num = 50 # global variable
userinput = int(input(" Enter Number: "))

def Check():
    if userinput == num:
        print(" It's equal to the variable")
    else:
        print(" It's not equal to the variable")
Check()
print("\n-----")
# change the value of a global variable inside a function

num2 = 800
def change():
    global num2
    num2 = 400
change()
print(num2)