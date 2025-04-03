class Solution(object):
    def removeDuplicates(self, nums):
        seen = set() 
        for num in nums:
            seen.add(num)  
        
        nums = seen
        return int(len(nums)) 

        
    
Solucion = Solution()
Array = [0,0,1,1,1,2,2,3,3,4]
print(Solucion.removeDuplicates(Array))

