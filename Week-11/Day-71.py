# Python Week-11 Day-71
# Python MySQL 2

import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("DROP DATABASE IF EXISTS Day73")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE Day73")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="Day73"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), age INT(2))")




mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address, age) VALUES (%s, %s, %s)"
val = [
  ('Peter', 'Lowstreet 4',25),
  ('Amy', 'Apple st 652', 25),
  ('Hannah', 'Mountain 21', 25),
  ('Michael', 'Valley 345', 25),
  ('Sandy', 'Ocean blvd 2', 25),
  ('Betty', 'Green Grass 1', 25),
  ('Richard', 'Sky st 331', 18),
  ('Susan', 'One way 98', 25),
  ('Vicky', 'Yellow Garden 2', 25),
  ('Ben', 'Park Lane 38', 25),
  ('William', 'Central st 954', 25),
  ('Chuck', 'Main Road 989', 25),
  ('Viola', 'Sideway 1633', 25),
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, " Row Was inserted.")
print(mycursor.lastrowid)


mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers WHERE name='Viola'")
for cost in mycursor.fetchall():
      print(cost)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers WHERE age=18")
for cost1 in mycursor.fetchall():
      print(cost1)

