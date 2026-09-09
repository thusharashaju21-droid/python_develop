


text= "England won by 6 wickes with 3 balls remaining. england leads the series with 2-1"
alpha_count=0
digit_count=0
special_character=0
for ch in text:
    if ch.isalpha():
        alpha_count=alpha_count+1
    elif ch.isdigit():
        digit_count=digit_count+1
    else:
        special_character=special_character+1
print("alphabet=💀",alpha_count)
print("digit=",digit_count)
print("special=",special_character)        
