"""
      *        r=6 space6   col1
     * *       r=5 space5   col2
    * * *      r=4 space4   col3
   * * * *     r=3 space3   col4
  * * * * *    r=2 space2   col5
 * * * * * *   r=1 space1   col5

"""

for r in range(6,0,-1):
    for space in range(1,r):
        print(" ",end="")
    for col in range(1,(7-r)+1):
      print("*",end=" ")    
    print()