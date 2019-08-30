

"""  عوامل الشروط المنطقية
 
  Python Logical Operators"""


My_Number = 8

method = """My_Number = 8
Method = My_Number > 7 or My_Number < 10
"""
print(method)

print("result = " , My_Number >7 or My_Number <10 )


print("\n"+"or"+"\n")

My_Number = 8

method = """My_Number = 8
Method = My_Number < 7 or My_Number > 10
"""
print(method)

print("result = " , My_Number < 7 or My_Number > 10 )

print("-----------------------------------------")

# Is العامل
# Is not العامل

M = "Apple, Samsung"
N = "Apple, Samsung"
B = "Huawei, Nokia"

Method1 = """M = "Apple, Samsung"
N = "Apple, Samsung"
B = "Huawei, Nokia"
"""
print(Method1)

print("result = ", B is not M)
print("result = ", M in N)
print("result = ", N  is not M)
print("result = ", B in N)