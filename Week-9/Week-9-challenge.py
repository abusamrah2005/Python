import json
import re


week_days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", )

print(type(week_days))

my_json = json.dumps(week_days)
print(my_json)
print("------")

str = "data is the new oil"
x = re.findall("data", str)
print("Search Result:", x)

print("------")
print("------")

python = {
  "language name": "Python",
  "Definition": "Python is an interpreted, high-level, general-purpose programming language",
  "Created by": "Guido van Rossum",
  "Date created": "first released in 1991",

}


print(json.dumps(python, indent=4))

