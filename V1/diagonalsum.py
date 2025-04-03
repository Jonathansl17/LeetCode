class Solution(object):
    def diagonalSum(self, mat):
        resultado = 0
        n = len(mat)
        
        for i in range(n):
            # Sumar el elemento de la diagonal principal
            resultado += mat[i][i]
            # Sumar el elemento de la diagonal secundaria
            resultado += mat[i][n - i - 1]
        
        # Si n es impar, restar el elemento central que se ha sumado dos veces
        if n % 2 != 0:
            resultado -= mat[n // 2][n // 2]
            
        return resultado

solucion = Solution()

matriz =[[1,2,3],
         [4,5,6],
         [7,8,9]]



print(solucion.diagonalSum(matriz))


