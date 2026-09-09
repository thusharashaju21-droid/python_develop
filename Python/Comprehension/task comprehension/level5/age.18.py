people = [("John",18),("Alice",22),("Bob",16),("Emma",25)]

result = [name for name, age in people if age >= 18]

print(result)