"""
Ask for PIN.

If PIN is correct:

Ask for withdrawal amount

If amount ≤ balance → "Withdrawal successful"

Else → "Insufficient balance"

Else → "Incorrect PIN" 
"""
db_pin=1233
db_amt=34500
pin=int(input("enter your pin"))
if pin==db_pin:
    amt=int(input("enter your amount"))
    if amt<= db_amt:
        print("Withdraw successfully")
    else:
        print("insufficient balance") 
else:
    print("incorrect pin")           