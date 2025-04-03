"""
       *       
      ***
     *****
    *******
   *********
  ***********
 *************
***************

n = 15
"""

def PrintTriangle(n):
    
    spaces = n- (n//2+1)
    for x in range(1,n+1):
        if x%2 != 0:
            print(" "*spaces +("*"*x)+ " "*spaces)
            spaces -=1

PrintTriangle(15)