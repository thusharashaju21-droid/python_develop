temp = [18,22,35,28,15]

result = ["Cold" if t < 20 else "Warm" if t < 30 else "Hot" for t in temp]

print(result)