from mysql import  connector
connection=connector.connect(
    user="root",
    password="Password@123",
    host="localhost",
    database="song_db"
)

cursor=connection.cursor()

query = """
update song set title=%s,singers=%s where id=%s
"""
values=("Cherathukal","Sushin Shyam",4)

cursor.execute(query,values)

connection.commit()

print("Record Updated...")