class Solution(object):
    @staticmethod
    def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        n = len(nums)

        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


# Input:
nums = [0, 1, 0, 3, 12, 2]
Solution.moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 2, 0, 0]