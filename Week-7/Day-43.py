# # Python Week-7 Day-43
# Python Inheritance

class Person: #------->  Super Class
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person): # ----> Sub Class
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname) 

x = Person ("\nPerson Class:  "+" Mohammed","Al Asmri" + " Called From Super Class( Person)")
x.printname()
y = Student("\nStudent Class: "+" Mohammed","Al Asmri" + " Called From Sub Class( Student)")
y.printname()
