# Python Week-7 Day-48
# Python Scope
# A variable created inside a function is available inside that function
print("\n-----")
def myfunc():
    x = "Python Scope"
    print (x)
myfunc()
print("\n-----")
# The local variable can be accessed from 
# a function within the function.
def myfunc1():
    xx = "Call Me"
    def myfunc2():
        print(xx)
    myfunc2()
myfunc1()
print("\n-----")
# cA variable created outside of a function is
#  global and can be used by anyone
y = "Global Variable"
def my_global():
    global yy # global variable Inside function
    yy = "variable inside function "
    print( y, " => inside function")
my_global() 

print("\n-----")
print(y, " => OutSide function")
print("\n-----")
print(yy) # print variable inside function


