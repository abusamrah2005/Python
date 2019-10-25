# Python Week-10 Day-66
# Python String Formatting 2

print("----")
brand = "Toyota"
model = "Corolla"
year = 2019
mycar = "I own a car from {0} Model {1} Year of manufacture {2}"
print(mycar.format(brand, model, year))
print("----")
brand = "Nissan"
model = "Maxima"
year = 2018
mycar = "I own a car from {1} Model {1} Year of manufacture {2}"
print(mycar.format(brand, model, year))
print("----")

mycar1 = "I own a car from {brand} Model {model} Year of manufacture {year}"
print(mycar1.format(brand = "KIA", model = "Cadenza", year = "2020"))