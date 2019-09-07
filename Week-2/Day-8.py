"""
The strip() method removes any whitespace from the beginning or the end
"""

print("لحذف أي مسافات فارغة في بداية ونهاية السلسلة النصية")

a = " I Love Python "
print("_I Love Python_")
print(a.strip()) # removes any whitespace

print("---------------------------------")
"""
The len() method returns the length of a string
لمعرفة عدد أحرف السلسة النصية استخدم الدالة len()
"""

b = "I Love Python"
print ("لمعرفة عدد أحرف السلسة النصية استخدم الدالة ")
print("I Love Python")
print("The number of characters is"), print(len(b))
print("---------------------------------")
"""
The lower() method returns the string in lower case.
الدالة lower() تقوم بترجيع النص بأحرف صغيرة
"""
m = "I LOVE PYTHON"
print(m)
print("تحويل النص من احرف كبيره الى احرف صغيره")
print(m.lower()) # method returns the string in lower case
print("---------------------------------")

"""
The upper() method returns the string in upper case.
الدالة upper() تقوم بترجيع النص بأحرف كبيرة
"""
n = "i love python"
print(n)
print("تحويل النص من احرف صغيره الى احرف كبيره")
print(n.upper())
print("---------------------------------")
# الدالة replace() تقوم بتبديل جزئية نصية بجزئية أخرى
#The replace() method replaces a string with another string.

k = "Tython, Lesson"
print(k)
print (" فيه خطا بحرفين نغير حرف T الى P")
print(k.replace("T", "P")) # method replaces a string with another string
print("---------------------------------")

"""
 The split() method splits the string into substrings
  if it finds instances of the separator.

  الدالة split() تقوم بتقسيم النص على حسب 
  الطريقة التي على أساسها تم استدعائها،
ثم يتم ترجيع النص على شكل مصفوفة نصوص.
"""
q = "python, language"
print(q)
print("الدالة split() تقوم بتقسيم النص على حسب")
print(q.split(","))