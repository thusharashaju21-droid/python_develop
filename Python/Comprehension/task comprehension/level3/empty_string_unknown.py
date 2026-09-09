names = ["John","","Alice","","David"]

result = ["Unknown" if len(n)==0 else n for n in names]

print(result)