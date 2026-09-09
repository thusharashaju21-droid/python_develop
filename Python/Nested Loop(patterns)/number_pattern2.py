"""
1  2  3  4  5
1  2  3  4 
1  2  3
1  2
1  


"""





def pattern2():
    for r in range(5,0,-1):
        for c in range(1,r+1):
            print(c,end="\t")
        print("")
pattern2()            