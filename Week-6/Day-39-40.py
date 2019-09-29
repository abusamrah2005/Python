# Python Week-6 Day-39-40 Challenge of the week6


def Challenge_Recursion(k, y):
    if(k > 0):
        result = k ** y
        print(result)
    else:
        result = 0
    return result

print("\n\nChallenge Recursion Results Finally its work")
Challenge_Recursion(5, 3)

print(" -----------  ")

print("Odd numbers Only")
x = [-4, -6, -5, -1, 2, 3, 7, 9, 88]
y = list( filter(lambda n: n%2==0,x))
print (y)
print(" -----------  ")
print("positive numbers Only")
numbers = [-4, -6, -5, -1, 2, 3, 7, 9, 88]
print("All numbers in the list: ",numbers)
my_numbers = list(filter(lambda x: x >0, numbers))
print("Positive numbers in My List : ",my_numbers)
