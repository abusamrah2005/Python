# Python Week-5 Day-28

# Python has two primitive loop commands.
# while loops.
# for loops.
print("---- Print i as long as i is less than 6 --")
i = 1
while i < 6 :
   print(i)
   i +=1 

print("---- Exit the loop when i is 3 ----")
i = 1
while i < 6 :
   print(i)
   if i == 3:
      break
   i += 1

print("----- Continue to the next iteration if i is 4 -----")
i = 0
while i < 6 :
   i += 1
   
   if i == 4:
      continue
   print(i)

print("---- -Print a message once the condition is false ---")
i = 1
while i < 7 :
   print(i)
   i += 1
else:
   print(" i is no longer less than 7 ")
