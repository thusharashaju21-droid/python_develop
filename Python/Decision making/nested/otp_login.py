"""Ask for password.

If password is correct:

Ask for OTP

If OTP is correct → "Login successful"

Else → "Incorrect OTP"


Else → "Incorrect password"
"""
db_pwd=00
db_otp=4567
pwd=input("enter your password")
if pwd==db_pwd:
    otp=int(input("enter your otp"))
    if otp==db_otp:

      print("Login succesfully")
    else:
       print("incoorect otp")
else:
   print("incorrect password")       

    