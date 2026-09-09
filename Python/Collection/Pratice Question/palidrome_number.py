words=["madam","tan","ant","racecar","malayalam"]
palidrome_word=[]
for w in words:
    reversed=w[::-1]
    if reversed==w:
     palidrome_word.append(w)
print(palidrome_word)     