text="A man, a plan, a canal panama"
#     01234567890123456789012345678
#               1         2
#extract canal
print(text[17:22])


#extract plan
substr1=text[9:13]
print(substr1)

#extract panama
substr2=text[23:29]
substr2=text[23:]
print(substr2)

#extract A man
substr3=text[:5]
print(substr3)

#copy
copy_str=text[:]
print(copy_str)