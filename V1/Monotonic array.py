class Solution(object):
    def isMonotonic(self, nums):
        
        if nums == sorted(nums,reverse=True) or nums == sorted(nums):
            return True
        
        else:
            return False
        
        
                    
        


Solucion = Solution()

Numbers = [1,2,2,3]


print(Solucion.isMonotonic(Numbers))