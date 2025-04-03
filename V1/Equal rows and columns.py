class Solution(object):
    def equalPairs(self, grid):
        counter = 0

        for x in range(len(grid[0])):
            New_Row = []
            
            for y in range(len(grid)):
                New_Row.append(grid[y][x])
            
            for row in grid:
                if row == New_Row:
                    counter += 1
        
        return counter
        
        
Solucion = Solution()

Matrix = [[3,2,1],[1,7,6],[2,7,7]]

print(Solucion.equalPairs(Matrix))



   