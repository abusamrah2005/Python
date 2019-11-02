import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

print(mydb)


# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Mohammed Al Asmri", "Tabuk")
mycursor.execute(sql, val)


mydb.commit()


print(mycursor.rowcount, "record inserted.")

mycursor.execute("SHOW DATABASES")
for x in mycursor:
      print(x)

mycursor.execute("SHOW TABLES")
for x in mycursor:
      print(x)
