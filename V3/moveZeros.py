class Solution(object):
    def moveZeroes(self, nums:list):

        for x in range(len(nums)-1,-1,-1):

            if(nums[x] == 0):
                nums.append(nums.pop(x))

        print(nums)
        
# Solucion = Solution()
# Zeroes = [0,0,1,3,0,0,7,5,4]
# Solucion.moveZeroes(Zeroes)
                
   
class Solution(object):
    def moveZeroes(self, nums):
        insert_pos = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        for i in range(insert_pos, len(nums)):
            nums[i] = 0

        print(nums)
Solucion = Solution()
Zeroes = [0,0,1,3,0,0,7,5,4]
Solucion.moveZeroes(Zeroes)