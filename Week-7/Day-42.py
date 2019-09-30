# # Python Week-7 Day-42
# Python Classes and Objects 2

print(" -- Let us create a method in the Person class --")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name )

p1 = Person("John", "36")
p1.myfunc()
print("----")

class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def myfunc(self):
        print("Car brand Is: " + self.brand, "\nCar Price Is: " + self.price)

p1 = Car("Kia", "10000")
p1.myfunc()

print("\n -- Modify Object Properties -- ")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.age = 40
print(p1.age)

print("\n -- Delete Object Properties --")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
try :
    del p1.age

    print(p1.age)
except AttributeError as err:
    print("Properties 'age' not Exist")


print("\n -- Delete Objects --")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1
try :
    print(p1.age)
except NameError as err:
    print("p1 is not Defined")
