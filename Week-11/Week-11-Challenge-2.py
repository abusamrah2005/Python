# Week-11 Challenge 2

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

print(mydb)

mycursor = mydb.cursor()
mycursor.execute("DROP DATABASE IF EXISTS MyEmployee")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE MyEmployee")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="MyEmployee"
)

mycursor = mydb.cursor()
mycursor.execute("DROP DATABASE IF EXISTS Employee")
mycursor.execute("CREATE TABLE Employee (id INT AUTO_INCREMENT PRIMARY KEY, FirstName VARCHAR(255), LastName VARCHAR(255), Age INT(2),Gender VARCHAR(255), Salary INT(5))")
mycursor = mydb.cursor()


mycursor = mydb.cursor()
sql = "INSERT INTO Employee (FirstName, LastName, age, Gender, Salary) VALUES (%s, %s, %s, %s, %s)"
val = [
  ('Ahmed', 'Ali', 30,  "male", 10000),
  ('Khalid', 'Muhammad', 34,  "male", 7000),
  ('Norah', 'Saleh', 29,  "female", 7000),
  ('Muhammad', 'Al Asmri', 38,  "male", 2500),
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, " Row Was inserted.")
print("Show All Rows")
sql = "SELECT * FROM Employee"

mycursor.execute(sql)

myresult = mycursor.fetchall()
for Employee in myresult:
    print(Employee)

print("------------")
print("\nShow FirstName,Gender And Salary\n")
sql = "SELECT FirstName,Gender,Salary FROM Employee"

mycursor.execute(sql)

myresult = mycursor.fetchall()
for Employee in myresult:
    print(Employee)

print("------------")
print("\nSort By FirstName\n")
sql = "SELECT * FROM Employee ORDER BY FirstName DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()
for Employee in myresult:
    print(Employee)

print("------------")
print("\nDelete Record\n")
sql = "DELETE FROM Employee WHERE Age = %s"
age = 34,
sql1 = "SELECT * FROM Employee"
mycursor.execute(sql, age)
mycursor.execute(sql1)
myresult = mycursor.fetchall()
for Employee in myresult:
    print(Employee)

