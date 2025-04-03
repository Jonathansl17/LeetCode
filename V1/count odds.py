class Solution(object):
    def countOdds(self, low, high):
        return (high + 1) // 2 - low // 2
        
        
Solucion = Solution()


From = 3
To = 7

print(Solucion.countOdds(From,To))