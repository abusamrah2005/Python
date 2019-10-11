# python Week-8 Day-53-54
# Week-8 Challenge
from Day54 import *
import datetime 
maths(num1, num2)


print("\n----------\n")
mathsum()
mathsub()
mathmult()
mathdivi()


print("\n----------------")

print("Date in Python\n")

today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1) 
print('Yesterday : ',yesterday)
print('Today : ',today)
print('Tomorrow : ',tomorrow)
