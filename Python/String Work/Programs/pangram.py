text="The quick brown fox jumps over the lazy dog."
alphabets="abcdefghijklmnopqrstuvwxyz"
for alpha in alphabets:
    if alpha not in text:
        print("not pangram")
        break
else:
    print("pangram")   
    
     