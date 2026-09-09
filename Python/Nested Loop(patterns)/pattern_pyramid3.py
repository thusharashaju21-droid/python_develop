"""

     *            r1 s=5 c=   
    * *           r2 s=4 c=
   *   *         r3 s=3 c=
  *     *       r4 s=2 c=
 *       *       r5 s=1 c=
* * * * * *      r6 s=0 c=

r+c==6 
c-r==4
r==5

  """

for r in range(1,6):
    for c in range(1,10):
        if r+c==6 or c-r==4 or r==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()            