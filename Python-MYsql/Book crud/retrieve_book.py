from mysql import connector

connection = connector.connect(
    user="root",
    password="Password@123",
    host="localhost",
    database="book_db"
)

cursor = connection.cursor()

query="select * from book where id =%s"

values=(1,)

cursor.execute(query,values)

book=cursor.fetchone()

print(book)