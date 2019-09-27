# Paython Week-6 Day-36
# Python Lambda 2
"""
The power of lambda is better shown when you use them
 as an anonymous function inside another function.
 """

def myfunc(n):
  return lambda a : a * n

print("-------")
def myfunc1(n):
      return lambda a : a * n

mydoubler = myfunc1(2)

print(mydoubler(11))

def myfunc(n):
      return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

print("\n--- use the same function definition to make both functions ----")

def myfunc(n):
      return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))