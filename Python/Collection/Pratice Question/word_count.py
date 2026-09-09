words = ["hai","hello","hai","hai","hai"]
word_set=set(words)
word_count={}
for w in word_set:
    word_count[w] = words.count(w)
print(word_count)    