from mysql import connector

connection = connector.connect(
    user="root",
    password="Password@123",
    host="localhost",
    database="book_db"
)

cursor = connection.cursor()

query = """
update book set title=%s, author=%s, price=%s where id=%s
"""

values = ("the alchemist", "paulo coelho", 400, 1)

cursor.execute(query,values)

connection.commit()

print("Book Updated")