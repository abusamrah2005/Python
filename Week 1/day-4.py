a = 10  # رقم صحيح 
b = 9.5 # رقم عشري
c = 1j  #  رقم مركب


print("a = 10 " +"  " + "رقم صحيح")
print("b = 9.5" +"  " +  "رقم عشري")
print("c = 1j" +"  " +  "رقم مركب")

print("--------------------")

print(type(a))
print(type(b))
print(type(c))

print("--------------------")

"""
التحويل بين الانواع
"""
x = float(a)       # التحويل من رقم صحيح الى رقم عشري
y = int(b)         # التحويل من عشري الى رقم صحيح
z = complex(a)     # التحويل من رقم صحيح الى رقم مركب
print("التحويل من رقم صحيح الى رقم عشري")
print(x)
print("--------------------")
print("التحويل من عشري الى رقم صحيح")
print(y)
print("--------------------")
print("التحويل من رقم صحيح الى رقم مركب")
print(z)

print("--------------------")

"""
العدد العشوائي

"""
import random

print(random.randrange (1,10))






input('Press ENTER to continue...')

