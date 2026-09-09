from mysql import  connector
connection=connector.connect(
    user="root",
    password="Password@123",
    host="localhost",
    database="song_db"
)

cursor=connection.cursor()

query="select * from song where id = %s"

values =(2,) # tuple

cursor.execute(query,values)

record=cursor.fetchone()

print(record)