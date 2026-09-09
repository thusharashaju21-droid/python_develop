"""
isalpha()
isalnum()
isdigit()

"""

password="Password@123"
if password.isalpha():
    print("Password is alphbet")
elif password.isalnum():
    print("Password is alphanumeric")
elif password.isdigit():
    print("Password is digit")
else:
    print("Special Character")