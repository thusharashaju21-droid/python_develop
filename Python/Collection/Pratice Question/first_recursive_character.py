text="ABCBAB"

#method1   #list

character_word=[]
for ch in text:
    if ch in character_word:
       print("first recursive number:",ch)
       break
    else:
        character_word.append(ch)

#method2   #dict  -/(imp)
# a-1 b-1 c-1
#b-2(display)
texxt="APCBAB"
char_count={}
for ch in texxt:
    if ch in char_count:
        print("first recursive number:",ch)
        break
    else:
        char_count[ch]=1




