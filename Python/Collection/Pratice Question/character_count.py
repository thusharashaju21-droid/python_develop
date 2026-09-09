word = "python programming is simple"
char_set=set(word)
char_count={}
for w in char_set:
    char_count[w] = word.count(w)
print(char_count)    
