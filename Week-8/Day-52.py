# Python Week-8 Day-52
# Python Datetime
import  datetime
x = datetime.datetime.now()
print(x)
print("-------")
print("-------")
# Return the year and name of weekday.
print(x.year)
print(x.strftime("%A"))
print("-------")
print("-------")
# Create a date object
x = datetime.datetime(2020, 5, 17)
print(x)
print("-------")
print("-------")
x = datetime.datetime(2019, 10, 10)
print(x.strftime("%B"))
print("-------")
print("-------")
x = datetime.datetime.now()
print(x.strftime("%Y"))
print("-------")
print("-------")
x = datetime.datetime.now()
print(x.strftime("%p"))
