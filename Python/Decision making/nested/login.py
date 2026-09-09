db_username="amritha"

db_password=2345

username=input("Enter user name:")

if username==db_username:
    password=int(input("Enter password"))
    if password==db_password:
        print("Login Successful")
    else:
        print("Invalid Password")
else:
    print("Invalid Usernme")

   