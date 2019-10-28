
# Python Week-11 Day-69
# File Handling in Python

print("-- Read Files --\n")
# read from file
x = open("Week-11/myfile.txt", "r")
print(x.read())
x.close()
print("----")
# read parts of the file
f = open("Week-11/myfile.txt", "r")
print(f.read(6))
print("----")
# read line
f = open("Week-11/myfile.txt", "r")
print(f.readline())
print("----")
# read 2 lines
f = open("Week-11/myfile.txt", "r")
print(f.readline())
print(f.readline())
print("----")
# line by line
f = open("Week-11/myfile.txt", "r")
for x in f:
  print(x)
f.close()
print("\n-- Write to File --\n")

y = open("Week-11/WriteToFile.txt", "a")
y.write("Hello World ")
y = open("Week-11/WriteToFile.txt", "r")
print(y.read())
f.close()
print("\n-- Create new File by user --\n")
# Create new File by user

file_name = input(" Enter file name to Create:  ")
full_name = file_name+".txt"
text_file = open("Week-11/"+full_name,"w")
print("Your file Created: "+full_name)

print("\n-- make user Write to file --")
# make user Write to file
name = input("ُEnter Your Name : ")
age = input("ُEnter Your Age : ")

f = open("Week-11/"+full_name, "a")
f.write(" Your Name Is " + name + "\n"+ " Your Age is "+ age + "\n")
f.close()

