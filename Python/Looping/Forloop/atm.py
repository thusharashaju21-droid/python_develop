db_pin=4714
for attempt in range(1,4):
    pin=input("enter the pin")
    if db_pin==pin:
        print("Atm pin unblocked successfully🎊")
        break
    else:
        print("Atm pin blocked")