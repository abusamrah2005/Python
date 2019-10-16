# Python Week-9 Day-55
# Python JSON2

import json

x = {
  "name": "Mohammed",
  "age": 38,
  "married": True,
  "divorced": False,
  "children": ("Abduallah","Danh", "Ahmad"),
  "pets": None,
  "cars": [
    {"model": "Malibu Chevrolet", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=2))
print("--------")
x = {
  "name": "Mohammed",
  "age": 38,
  "married": True,
  "divorced": False,
  "children": ("Abduallah","Danh", "Ahmad"),
  "pets": None,
  "cars": [
    {"model": "Malibu Chevrolet", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=2, separators=(". ", " --> ")))
print("--------")
x = {
  "name": "Mohammed",
  "age": 38,
  "married": True,
  "divorced": False,
  "children": ("Abduallah","Danh", "Ahmad"),
  "pets": None,
  "cars": [
    {"model": "Malibu Chevrolet", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=2, sort_keys=True))