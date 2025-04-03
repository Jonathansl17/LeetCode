class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pointer1 = 0
        pointer2 = -k
        
        for x in range(pointer2,pointer1):
            nums[pointer1],nums[pointer2] = nums[pointer2], nums[pointer1]
            
            pointer1 +=1
            pointer2 +=1
        
        
        print(nums)
        
        
        
sol = Solution()
nums = [1,2,3,5,6,7]
k = 2
sol.rotate(nums, k)