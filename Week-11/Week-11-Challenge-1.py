# Week-11 Challenge 1 And Extra Challenge

x = open("Week-11/Week-11-Challenge.txt", "r")
print(x.read())
x.close()

print("\n-*-*-*-*-*-*")
print("-*-*-*-*-*-*")
print("-*-*-*-*-*-*\n")
y = open("Week-11/Week-11-Challenge.txt", "a")
y.write("\nThe best way we learn anything is by practice and exercise questions ")
y = open("Week-11/Week-11-Challenge.txt", "r")
print(y.read())
y.close()

print("\n-*-*-*-*-*-*")
print("-*-*-*-*-*-*")
print("-*-*-*-*-*-*\n")

f = open("Week-11/readline.txt", "r")
print(f.readlines())
f.close