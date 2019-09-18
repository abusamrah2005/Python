# # Python Week-5 Day-29
# Python Loops 2

print("---- The For Loops ----")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

  print("--- Looping Through a String ----")

  for x in "cherry":
      print(x)

print("--- The break Statement ---")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
print("---")

for x in fruits:
    print(x)
    if x == "banana":
      break

print("--- The continue Statement ---")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


