class Solution(object):
    def rotate(self, matrix):
        
        n = len(matrix)
        #Trasponer
        for x in range(n):
            for y in range(x,n):
                matrix[x][y],matrix[y][x] = matrix[y][x],matrix[x][y]
        print(matrix)
        
        #Invertir
        for x in range(n):
            for y in range(n // 2):
                matrix[x][y], matrix[x][n - y - 1] = matrix[x][n - y - 1], matrix[x][y]
        
        return matrix
            
 
                
        
       
        
Solucion = Solution()


Matriz = [[1,2,3,1],
          [4,5,6,6],
          [7,8,9,8]]

print(Solucion.rotate(Matriz))


[[1, 4, 7, 1], 
 [2, 5, 8, 6],
 [3, 6, 9, 8]]

[[7, 4, 1, 1], 
 [8, 5, 2, 6],
 [9, 6, 3, 8],
 [1, 4, 7, 1], 
 [2, 5, 8, 6],
 [3, 6, 9, 8]]