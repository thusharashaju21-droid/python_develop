word="supercalifragilisticexpialidocious"
vowel_count=0
for ch in word:
    if ch.lower() in "aeiou":
        vowel_count=vowel_count+1
print(vowel_count)        