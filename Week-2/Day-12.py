


print("""Please, I want {} sandwishes and {} donutes 
-- استبدال حرف الضمير i بحرف we باستخدام دالة الاستبدال 
--- في الأقواس الخالية وباستخدام الدالة
 المناسبة قم بمليء الفراغ الأول ب العدد 5 والفراغ الثاني بالعدد
7 
--- حوّل كل حرف “a” إلى كابيتال )حرف كبير( Capital Letter """)

print("-----------------------------------------------")
print("-----------------------------------------------")

print("""
sandwishes = 5
donutes = 7
My_Order = " Please, I want {} sandwishes and {} donutes "
""")
sandwishes = 5
donutes = 7
My_Order = " Please, I want {} sandwishes and {} donutes "

print("resulte : " ,My_Order.format (sandwishes, donutes).replace("I", "we").replace("a", "A"))

