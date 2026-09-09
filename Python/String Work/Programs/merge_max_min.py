w1="PQRS"
w2="ABCDE"
large_word=max(w1,w2,key=len)
small_word=min(w1,w2,key=len)
merged_str=""
for i in range(0,len(small_word)):
    merged_str+=w1[i]+w2[i]
balance=large_word[len(small_word):]
merged_str+=balance
print(merged_str)    


