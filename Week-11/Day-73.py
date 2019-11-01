# Python Week-11 Day-73
# Python MySQL 4

import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("DROP DATABASE IF EXISTS LastDay")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE LastDay")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="LastDay"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), age INT(2), vehicle INT(5))")
mycursor = mydb.cursor()

print("-------")



mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address, age, vehicle) VALUES (%s, %s, %s, %s)"
val = [
  ('Peter', 'Lowstreet 4', 25,  1),
  ('Amy', 'Apple st 652', 25,  3),
  ('Hannah', 'Mountain 21', 25,  5),
  ('Michael', 'Valley 345', 25,  4),
  ('Sandy', 'Ocean blvd 2', 25,  6),
  ('Betty', 'Green Grass 1', 25,  9),
  ('Richard', 'Sky st 331', 18, 11),
  ('Susan', 'One way 98', 25,  8),
  ('Vicky', 'Yellow Garden 2', 25,  13),
  ('Ben', 'Park Lane 38', 25,  12),
  ('William', 'Central st 954', 25,  41),
  ('Chuck', 'Main Road 989', 25,  7),
  ('Viola', 'Sideway 1633', 25,  10),
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, " Row Was inserted.")
print("-------")


mycursor = mydb.cursor()
sql = "UPDATE customers SET address = 'KSA ABHA' WHERE address = 'Sideway 1633' "
sql1 = "UPDATE customers SET age = 38 WHERE address = 'KSA ABHA' "

mycursor.execute(sql)
mycursor.execute(sql1)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
print("--------")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for update in myresult:
    print(update)

print("--------")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 8")
myresult = mycursor.fetchall()
for limit in myresult:
    print(limit)

print("--------")
print("--------")
print("--------")

mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS products")

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, car VARCHAR(255), model VARCHAR(255))")
mycursor = mydb.cursor()


print("-------")

mycursor = mydb.cursor()
sql = "INSERT INTO products (car, model) VALUES (%s, %s)"
val = [
  ('TOYOTA', ''),
  ('BMW',    ''),
  ('Audi', ''),
  ('Chevrolet', ''),
  ('Ferrari', ''),
  ('Chrysler', ''),
  ('Ford', ''),
  ('Honda', ''),
  ('GMC', ''),
  ('Genesis', ''),
  ('Alfa-Romeo', ''),
  ('Infiniti', ''),
  ('Lamborghini', ''),
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, " Row Was inserted.")
print("-------")

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM products")
myresult = mycursor.fetchall()
for prod in myresult:
    print(prod)

print("-------")
print("-------")


sql = "SELECT \
  customers.name , \
  products.car \
  FROM customers \
  INNER JOIN products ON customers.vehicle = products.id"
mycursor.execute(sql)
myresult1 = mycursor.fetchall()
for x in myresult1:
  print(x)

print("-------")
print("-------")
