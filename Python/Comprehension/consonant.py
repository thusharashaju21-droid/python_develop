text="a new a canal panama"
consonant={ch for ch in text if ch not in "aeiou" and ch.isalpha()}
print("consonant",consonant)