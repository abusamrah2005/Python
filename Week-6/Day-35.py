# Paython Week-6 Day-35
# Python Lambda

print("\n---- Python Lambda ----\n")
x = lambda a : a + 10
print(x(5))

print("\n---- Lambda functions take any number of arguments. ----\n")

x = lambda z, s : z * s
print(" tow numbers: ", x(4, 5))

print(" ----- ")

x = lambda a, b, c : a + b + c
print(" Three numbers: ", x(5, 6, 2))

print("\n------| Examples |--------")

print("1- ", (lambda a : a + 10)(5))
print("2- ", (lambda z, s : z * s)(10, 5))
print("3- ", (lambda a, b, c : a + b + c)(2, 4, 5))


