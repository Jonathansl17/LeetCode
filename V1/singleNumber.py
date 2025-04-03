class Solution(object):
    def singleNumber(self, nums):
    
        frecuencies = {}
        
        for x in nums:
            if x in frecuencies:
                frecuencies[x] += 1
            else:
                frecuencies[x] = 1
                
        for x,y in frecuencies.items():
            if y ==1:
                return  x
        
        
x = Solution()


ys = [2,2,3]
print(x.singleNumber(ys))