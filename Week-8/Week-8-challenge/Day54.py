# python Week-8 Day-53-54
# Week-8 Challenge
def mathsum ():
    sum = 1 + 8
    print(sum)

def mathsub():
    sub = 4 - 2
    print(sub)

def mathmult ():
    mult = 6 * 6
    print(mult)

def mathdivi():
    divi = 8 / 2
    print(divi)

num1 = int(input(" Enter Num1: "))
num2 = int(input(" Enter Num2: "))
opr = input(" Enter operation Type (+, -, *, /): ")

def maths(num1, num2):
        if opr == "+" :
            res = num1 + num2
            print(res)
        elif opr == "-" :
            res = num1 - num2
            print(res)
        elif opr == "*" :
            res = num1 * num2
            print(res)
        else:
            res = num1 / num2
            print(res)

# maths(num1, num2)
