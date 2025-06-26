import mysql.connector

db1=mysql.connector.connect(
  host='localhost',
  user='root',
  password='Chaitrraa*45'  
)

print(db1)

cursor1=db1.cursor()
cursor1.execute('CREATE DATABASE smdb6')

