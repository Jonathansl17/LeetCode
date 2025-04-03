class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):

        result = []
        maxx = 0
        for x in candies:
            if x > maxx:
                maxx = x
        
        for x in candies:
            result.append(x + extraCandies >= maxx)    
    
        return result
        
x = Solution()

Kids =[7,2,5,6,9,9,4,5]
Candies = 3

print(x.kidsWithCandies(Kids,Candies))