text="Hello@wOrld#"
vowels=[]
constants=[]
special=[]
for ch in text:
    if ch.lower() in "aeiou":
        vowels.append(ch)
    elif ch.isalpha():
        constants.append(ch) 
    else:
        special.append(ch) 
print("vowels=",vowels)
print("constants'",constants)
print("special=",special)           

