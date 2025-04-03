class Solution(object):
    @staticmethod
    def isMonotonic(nums):
        original = [x for x in nums]
        
        for i in range(len(nums)):
            
            min_Index = i
            
            for j in range(i+1, len(nums)):
                
                if(nums[min_Index] > nums[j]):
                    
                    min_Index = j
                    
            nums[i],nums[min_Index] = nums[min_Index],nums[i]
        
        reversed = []
        
        for x in range(len(nums)-1,-1,-1):
            reversed.append(nums[x])
                    
        print(reversed)
        
        print(original)
        print(nums)
        return original == nums or original == reversed



print(Solution.isMonotonic([1,3,2]))