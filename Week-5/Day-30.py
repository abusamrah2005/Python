# Python Loops 3

print("--- Using the range() function ---")

for x in range(11):
    print (x)

print("--- Using the start parameter ---")

for w in range(3,9):
    print(w)

print("--- Increment the sequence with 6 (default is 1) ---")

for q in range(6, 20, 4):
    print(q)

print("--- Print all numbers from 0 to 5, and print a message when the loop has ended ---")

for g in range(9):
    print(g)
else:
    print("Finally Finished")
    
print("\n--- Print each adjective for every fruit ---")

color = ["Red", "Orange", "Yellow"]
fruits = ["apple", "banana", "cherry"]
for T in color:
    for Y in fruits:
        print (T, Y)
