class Solution(object):
    def checkStraightLine(self, coordinates):
        
        listed = []
        listed2 = []
    
        for y in range(len(coordinates[0])):
            
            for x in range(len(coordinates)):
                
                if y == 0:
                    listed.append(coordinates[x][y])

                else:
                    listed2.append(coordinates[x][y])
            
        Tres = map(lambda x: x + 1, listed)
 
        return True if list(Tres) == listed2 else False


        
Solucion = Solution()

Numeros = [[1,2],
           [2,3],
           [3,4],
           [4,5],
           [5,6],
           [6,7]]

print(Solucion.checkStraightLine(Numeros))

