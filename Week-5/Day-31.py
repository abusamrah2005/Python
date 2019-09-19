# Python Week-5 Day-31

# Python Functions

# Creating a Function -- In Python a function is defined using the def keyword


def my_function():
    print(" This Is My First Function ")

# To call a function, use the function name followed by parenthesis


my_function()

# Parameters
print("----")


def country(name, age, country1):
    print('I am from', name)
    print('I am ', age, 'old')
    print("I am From ", country1)


while True:
    name = input("Enter Your Name: ")
    age = int(input("Enter Your Age : "))
    country1 = input(" Where Are You From: ")


    country(name, age, country1)
  
    if age <= 25:
        print(name, "you're a young man")
    elif age > 25 and age < 41:
        print(name, " You Are middle age")
    else:
        print(name, "You are old")
