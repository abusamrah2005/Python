# Python Week-9 Day-55
# Python Regular Expressions (RegEx)
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if (x):
  print("YES! We have a match!")
else:
  print("No match")
print("---")
str = "My Name is Mohammed"
x = re.findall("Mohammed", str)
print("we Found Your Name In str ", x)
print("---")
str = "My Name is Mohammed"
x = re.findall("Name", str)
print(x)
print("---")
str = "My Name is Mohammed"
x = re.findall("Abduallah", str)
print(" The Name Not Exist in str", x)
print("----")
str = "My car Is Malibu"
x = re.split("\s", str, 1)
print(x)
print("----")
str = "My car Is Malibu"
x = re.sub("\s", " <-> ", str)
print(x)
