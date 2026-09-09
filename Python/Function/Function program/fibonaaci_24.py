def fibonaaci_num(num):
    frst = 0
    second = 1
    next = 1

    while(next <= num):
        next = frst + second
        if next == num:
            print(True)
            break
        frst = second
        second = next
    else:
        print(False)

fibonaaci_num(16)
fibonaaci_num(21)