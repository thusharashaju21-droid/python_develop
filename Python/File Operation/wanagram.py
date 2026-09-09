words = ["silent","listen","race","care","trap","night","tight"]

fw = open("Python\\File Operation\\anagram.txt", "w")

for wi in words:
    for wj in words:
        if sorted(wi) == sorted(wj) and wi != wj:
         fw.write(wi+"\n")
