class Solution(object):
    def setZeroes(self, matrix):
        
        #Longitud de la matriz
        longitudFilas = len(matrix)
        longitudColumnas = len(matrix[0])
        
        #Crear matriz de booleanos para evitar marcaciones de mas
        booleanMatrix = [[False for _ in range(longitudColumnas)] for _ in range(longitudFilas)]

        #Marcar la matriz de booleanos
        for i in range(longitudFilas):
            for j in range(longitudColumnas):
                
                #Si es 0, marcamos las filas y columnas
                if(matrix[i][j] == 0):

                    # Marcar filas
                    for x in range(longitudColumnas):  
                        booleanMatrix[i][x] = True

                    # Marcar columnas
                    for k in range(longitudFilas):  
                        booleanMatrix[k][j] = True

        #Convertir la matriz usando la boolean matrix
        for x in range(longitudFilas):
            for y in range(longitudColumnas):
                if(booleanMatrix[x][y]):
                    matrix[x][y] = 0
        
        #retornamos la matriz ya con los 0s cambiados    
        return matrix


Matriz = [[1,1,1],
          [1,0,1],
          [1,1,1]]

Sol = Solution()
NewMatrix = Sol.setZeroes(Matriz)

for x in NewMatrix:
    print(x)
