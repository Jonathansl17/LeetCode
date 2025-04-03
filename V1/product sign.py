class Solution(object):
    def arraySign(self, nums):
        
        result = 1
        
        for x in nums:
            result *=x
        
        if result <= 0:
            return 0 if result == 0 else -1
             
        return 1

Solucion = Solution()

Numbers = [1,5,0,2,-3]


print(Solucion.arraySign(Numbers))