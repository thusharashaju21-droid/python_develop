#step 1 : import connector from mydql module
from mysql import connector

# step 2: establish a connection 

connection=connector.connect(
    user="root",
    password="Password@123",
    host="localhost"
)

print(connection)

