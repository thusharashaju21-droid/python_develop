def product(*args):
    result=1
    for num in args:
        result=result*num
    return result
print(product(2,4,6))
print(product(3,2))
