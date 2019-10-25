# Python Week-10 Day-65
# Python String Formatting

price = 49
price1 = 12.50
txt = " Te Price is {} Dollars"
print(txt.format(price))
print(txt.format(price1))
print("----")
txt = " Te Price is {:.2f} Dollars"
print(txt.format(price))
print("----")
brand = "Toyota"
model = "Corolla"
year = 2019
mycar = "I own a car from {} Model {} Year of manufacture {}"
print(mycar.format(brand, model, year))
print("I have {}".format(brand), "Model {}".format(model), "Year of manufacture {}".format(year))
