def is_pangram(text):
    alphabets="abcdefghijklmnopqrstuvwxyz"
    for alpha in alphabets:
     if alpha not in text.lower():
        print(False)
        break
    else:
      print(True)   
is_pangram("The quick brown fox jumps over the lAzy dog.")      
