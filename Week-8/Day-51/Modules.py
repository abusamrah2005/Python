import platform
import mymodules as mx

a = mx.person1["age"]
print(a)
print("----")
print("----")
x = platform.system()
xx = platform.python_version()
xxx = dir(platform)
print(" My Operating System is", x)
print(" Python Version", xx)
print (xxx)
print("----")
print("----")
# for items in xxx:
#     print(items)