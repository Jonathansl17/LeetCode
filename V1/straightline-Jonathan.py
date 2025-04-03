class Solution(object):
    def checkStraightLine(self, coordinates):

        for x in range(len(coordinates)-1):
            
            if coordinates[x][1] == coordinates[x+1][0]:
                continue
            else:
                return False
        
        return True
                


        
Solucion = Solution()

Numeros =[  [0,0],
          [0,1],
        [0,-1]]

print(Solucion.checkStraightLine(Numeros))

