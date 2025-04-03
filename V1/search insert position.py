class Solution(object):
    def searchInsert(self, nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + ((high - low) // 2)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low
        
Solucion = Solution()

NUMBERS = [1,2,3,5,6]
target = 4

print(Solucion.searchInsert(NUMBERS,target))