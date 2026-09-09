text="listen"
word="silent"
for ch in text:
    if ch not in word or text.count(ch)!=word.count(ch):

        print("Not Anagram")
        break   
else:
    print("Anagram")    