"""
word1="PQR"
word2="ABC"
merge_string="PQRABC"


"""
word1="PQRS"
#      0123

word2="ABCD"
#      01234
merged_str=""
for i in range(0,len(word1)):
    merged_str+=word1[i]+word2[i]
print(merged_str)    