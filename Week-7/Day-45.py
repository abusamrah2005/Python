# Python Week-7 Day-44
# Python Iterators

mytuple = ( "cherry", "apple", "banana")
myiter = iter(mytuple)
print(next(myiter), next(myiter), next(myiter))


print(" --- ")
# Strings are also iterable objects, containing a sequence of characters.
mystr = "TOYOTA"
my_iter = iter(mystr)
print(next(my_iter), next(my_iter), next(my_iter), next(my_iter), next(my_iter), next(my_iter))

print(" --- ")
# Iterate the values of a tuple.
mytu = ("BMW", "KIA", "NISSAN")
for x in mytu:
  print(x)

print(" --- ")

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter), next(myiter), next(myiter), next(myiter), next(myiter))

