class Solution(object):
    def plusOne(self, digits):

        for x in reversed(range(len(digits))):
            
            if digits[x] == 9:
                digits[x] = 0
                
            else:
                digits[x]+=1
                return digits
            
        return [1] + digits
                
            

Solucion = Solution()


Numbers = [1,2,8]
print(Solucion.plusOne(Numbers))
