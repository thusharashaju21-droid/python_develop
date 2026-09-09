"""
display prime number 5 to 20
"""



for num in range(5,21):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)    