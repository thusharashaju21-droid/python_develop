"""
*  *  *  *  *  * r6 space=0  c6
 *  *  *  *  *    r5 space=1  c5
  *  *  *  *       r4 space=2  c4
   *  *  *        r3 space= 3   c3
     * *          r2  space=4   c2
      *           r1   space=5  c1


"""

for r in range(6,0,-1):
    for space in range(1,(6-r)+1):
        print(" ",end="")
    for c in range(1,r+1):
            print("* ",end="")
    print()        