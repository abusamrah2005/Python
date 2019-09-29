# Python Week-7 Day-41 
# Python Classes and Objects
# To create a class, use the keyword class
print("\n------ \n")
class myfirstclass:
    x = 10
print (myfirstclass)
p1 = myfirstclass()
print(p1.x)

print("\n------\n")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Mohammed", 39)
print (p1.name)
print(p1.age)
print("\n------\n")

class art:
    def __init__(self, music, paint):
        self.music = music
        self.paint = paint
print("--- user insert info ---")
ww = input(" your Favorite Music : ")
ee = input(" your Favorite art : ")
print("--- result ---")
print(" Mohammed Favorite Music is: ", ww)
print(" Mohammed Favorite drawing is: ", ee)

