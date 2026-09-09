words = ["hello","hai","hello","wow","silent","active","hello"]

wc = {w:words.count(w) for w in set(words)}

print(wc)


