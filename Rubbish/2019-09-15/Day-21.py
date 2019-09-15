# Python Week4 Day-21
# المجموعات في لغة البايثون
# Python Sets 2
print("\n-------------Length--------------------\n")
# Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print("Number of Items in set : ", len(thisset))
print("\n----------Remove Item------------------\n")
# Remove Item
thisset1 = {"apple", "banana", "cherry"}
# ser = input("Please Enter Item Name : ")
# if ser not in thisset1:
thisset1.remove("apple")
#     print("item not Exist")
# else:
print(thisset1)
print("\n-------------discard()-----------------\n")
# Remove "banana" by using the discard() method.
thisset2 = {"apple", "banana", "cherry"}
thisset2.discard("banana")
# thisset2.discard("ban") Note: If the item to remove does not exist, discard() will NOT raise an error.
print(thisset2)
print("\n----------------pop()------------------\n")
# Remove the last item by using the pop() method.
thisset3 = {"apple", "banana", "cherry"}
x = thisset3.pop()
print(x) #removed item
print(thisset3) #the set after removal
print("\n----------------clear()------------------\n")
# The clear() method empties the set.
thisset4 = {"apple", "banana", "cherry"}
thisset4.clear()
print(thisset4)
print("\n----------------del------------------\n")
thisset = {"apple", "banana", "cherry"}
del thisset
#print(thisset) #this will raise an error because the set no longer exists
print("\n----------------set()------------------\n")
thisset5 = set(("apple", "banana", "cherry")) 
print(thisset5)
