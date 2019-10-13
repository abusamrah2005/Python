# Python Week-9 Day-55
# Python JSON

import json

print("\n---------")
x =  '{ "name":" Mohammed", "age":38, "city":" Abha"}'

y = json.loads(x)
print(y["age"])
print("---------")
x = {
  "name": " Mohammed Asmri",
  "age": 38,
  "city": " Yanbu"
}
y = json.dumps(x)
print(y)
print("---------")

print(json.dumps({"name": " Ahmad", "age": 3}))
print(json.dumps([" Toyota", " BMW"]))
print(json.dumps((" apple", " bananas")))
print(json.dumps(" Welcome Home"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
print("---------")
x = {
  "name": "Mohammed",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Abduallah","Danh", "Ahmad"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))