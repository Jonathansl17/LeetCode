class Solution(object):
    def majorityElement(self, nums):
        Numbers = {}   
        
        for x in range(len(nums)):              
            Numbers[nums[x]] = Numbers.get(nums[x], 0) + 1

        print(Numbers)
        for x,y in Numbers.items():
            if y == max(x for x in Numbers.values()):
                return x
        
        
        
Solucion = Solution()

Numeros = [3,2,3,1,1,1]

print(Solucion.majorityElement(Numeros))