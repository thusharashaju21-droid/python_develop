def fibonacci(num):
    first = 0
    second = 1

    for i in range(num):
        print(first)
        next = first + second
        first = second
        second = next

fibonacci(10)