"""
5       5       5       5       5
4       4       4       4
3       3       3
2       2
1

"""




def number_pattern():
 for r in range(5,0,-1):
    for c in range(1,r+1):
        print(r,end="\t")
    print("")
number_pattern()        