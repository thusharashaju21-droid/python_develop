from mysql import connector

connection = connector.connect(
    user="root",
    password="Password@123",
    host="localhost",
    database="book_db"
)

cursor=connection.cursor()

query="insert into book(title,author,price) values(%s,%s,%s)"

values=("book4","name4",450)

cursor.execute(query,values)

connection.commit()

print("Book Inserted")