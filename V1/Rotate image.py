class Solution(object):
    def rotate(self, matrix):

        
        Final = []
        
        for i in range(len(matrix[0])-1,-1,-1):
            
            NewRow = []
            
            for j in range(len(matrix)-1,-1,-1):
                
                NewRow.append(matrix[j][i])
                
            Final.append(NewRow)
        
        return Final[::-1]
        
Solucion = Solution()


Matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(Solucion.rotate(Matriz))

