words = ["silent","listen","act","cat","note","tone","hen","chicken"]

anagram = set() #no duplicates           

for i in range(0,len(words)):

    for j in range(0,len(words)):

        w1 = words[i]

        w2 = words[j]

        if sorted(w1) == sorted(w2) and w1!= w2:

            anagram.add(w1)

            anagram.add(w2)

print(anagram)            