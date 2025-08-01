class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 1
        for x in range(len(nums)):
            result *= nums[x]

        if result > 0:
            return 1
        
        if result < 0:
            return -1

        return 0
                    




nums = [1,5,0,2,-3]
Solucion = Solution()
print(Solucion.arraySign(nums))