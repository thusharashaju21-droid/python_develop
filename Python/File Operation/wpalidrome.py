words = ["madam","aba","tan","sin","malayalam"]

fw = open("Python\\File Operation\\palidrome.txt", "w")

for w in words:
    reversed = w[::-1]

    if reversed == w:
        fw.write(str(w)+"\n")

