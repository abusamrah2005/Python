# Python Week-10 Day-64
# Python Try-Except


try:
    print(x)
except  NameError as err:
    print ("name 'x' is not defined")
print("----")
try:
    print("Welcome To My Code")
except  NameError as err:
    print("Something went wrong")
else:
    print("Complete no errors")

print("----")
try:
    print(x)
except  NameError as err:
    print ("name 'x' is not defined")
finally:
    print(" The Try Except Is Finished")

