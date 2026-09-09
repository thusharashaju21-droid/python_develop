def is_anagram(text,word):
  
  text=text.lower()
  word=word.lower()
  
  for alpha in text:
     
     if alpha not in word or text.count(alpha)!=word.count(alpha):

        print(False)

        break  
      
  else:
     
     print(True) 

is_anagram("Listen","Silent")   
is_anagram("listen","silent") 