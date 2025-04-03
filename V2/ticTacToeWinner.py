class Solution(object):
    def tictactoe(self, moves):
        n = len(moves)
        
        matrix = [['' for _ in range(3)] for _ in range(3)]

        # Usar matriz auxiliar
        for i in range(n):
            matrix[moves[i][0]][moves[i][1]] = 'x' if i % 2 == 0 else 'o'

        # Verificar gane en filas
        for i in range(3):
            if matrix[i][0] == matrix[i][1] == matrix[i][2] and matrix[i][0] != '':
                return 'A' if matrix[i][0] == 'x' else 'B'

        # Verificar gane en columnas
        for i in range(3):
            if matrix[0][i] == matrix[1][i] == matrix[2][i] and matrix[0][i] != '':
                return 'A' if matrix[0][i] == 'x' else 'B'

        # Verificar gane en diagonales
        if matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[0][0] != '':
            return 'A' if matrix[0][0] == 'x' else 'B'
        if matrix[0][2] == matrix[1][1] == matrix[2][0] and matrix[0][2] != '':
            return 'A' if matrix[0][2] == 'x' else 'B'

        # Verificar si el juego está pendiente o es un empate
        if n == 9:
            return 'Draw'
        else:
            return 'Pending'

moves = [[0,0],[1,2],[0,2],[1,1],[2,0],[1,0],[2,1],[0,1],[2,2]]
sol = Solution()
print(sol.tictactoe(moves))  