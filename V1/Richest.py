class Solution(object):
    def maximumWealth(self, accounts):

        Richest = sum(accounts[0])
        
        for x in range(len(accounts)):
            
            if sum(accounts[x]) > Richest:
                Richest = sum(accounts[x])
                    
    
        return Richest
    
    
Solucion = Solution()

Customers = [[1,2,3],[3,2,1]]

print(Solucion.maximumWealth(Customers))