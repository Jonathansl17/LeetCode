class Solution(object):
    def moveZeroes(self, nums):
        for x in range(len(nums)-1, -1, -1):
            if nums[x] == 0:
                nums.append(nums.pop(x))
        print(nums)

Solucion = Solution()
Zeroes = [0,0,1,3,0,0,7,5,4]
Solucion.moveZeroes(Zeroes)
                
   
