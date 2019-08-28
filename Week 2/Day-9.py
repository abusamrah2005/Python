
# String Format
# تنظيم/تنسيق النصوص

"""
We can combine strings and numbers by using the format() method
يمكنك الدمج بينهم بواسطة دالة format() فهي تستخدم لإجراء عملية التنسيق على النص

"""

Age = 38
text = "My Name is Mohammed, I am {}"

print(text.format(Age))

print("-------------------------------")

print("format() method")
print("My_Order = I want {} pieces of Item {} for price {} dollars .")
qount = 200
item = "CD"
price = 2
My_Order = " I want {} pieces of Item {} for price {} dollars ."

print(My_Order.format(qount, item, price))

print("-------------------------------")

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders

print("You can use index numbers {0} to be sure the arguments are placed in the correct placeholders")
qount = 200
item = "CD"
price = 2
My_Order = " I want {1} pieces of Item {0} for price {2} dollars "

print(My_Order.format(qount, item, price))

print("-------------------------------")
