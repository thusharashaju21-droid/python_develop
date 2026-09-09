"""

word1="PQRST"
       01234
word2="ABC 
       012
PAQBRC             


"""
word1="PQRST"
word2="ABC"
small_str=""
large_str=""
merge_str=""
if len(word1)<len(word2):
    small_str=word1
    large_str=word2
else:
    small_str=word2
    large_str=word1
for i in range(0,len(small_str)):
    merge_str+=word1[i]+word2[i] 
balance=large_str[len(small_str):]
merge_str+=balance           
print(merge_str)