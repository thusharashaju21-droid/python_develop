"""
    *  r1 4 space 1c     (6 row=-5-1+1)
   **  r2  3 space 2 c
  ***  r3  2 space 3c
 ****  r4  1 space 4c
*****  r5  0space  5c

"""


for r in range(6, 0, -1):
    for space in range(1, r):
        print(" ", end="")

    for c in range(1, (7- r) + 1):
        print("*", end="")

    print()

