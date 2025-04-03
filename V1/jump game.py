class Solution(object):
    def canJump(self, nums):
        
        n = len(nums)
        
        goal = n-1
      
        
        for i in range(n-1,-1,-1):
            
            maxJump = nums[i]
            
            if i + maxJump >= goal:
                goal = i
                
                
        if goal == 0:
            return True
                
        else:
            return False
            
            
            
        
x = Solution()

array = [2,3,1,6,4]

print(x.canJump(array))