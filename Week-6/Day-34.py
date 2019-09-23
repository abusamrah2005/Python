# Paython Week-6 Day-34
# Python Functions 2

print("---- Passing a List as a Parameter ----")
def my_func(food):
    for x in food:
        print(x)

My_Cart = ["apple", "banana", "cherry"]

my_func(My_Cart)


print("---- To let a function, return a value, use the return statement ----")

def ret_value(b):
    return 5 * b

print(" value = ", ret_value(3))
print(" value = ", ret_value(4))
print(" value = ", ret_value(5))

print("---- Keyword Arguments ----")

def my_childs(child1, child2, child3):
    print(" The Youngest child is " + child3)
my_childs(child1 = " Abduallah", child2 = " Danh", child3 = " Ahmed")

print("---- If the number of arguments is unknown, add a * before the parameter name. ----")

def my_childs1(*kids):
    print(" The Youngest child is " + kids[0])
    print(" The Youngest child is " + kids[1])
    print(" The Youngest child is " + kids[2])
my_childs1(" Abduallah", " Danh", " Ahmed")

print("---- Python also accepts function recursion ----")


def Tri_Recursion(k):
    if(k > 0):
        result = k + Tri_Recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
Tri_Recursion(6)
