class Solution(object):
    def reverse(self, x):

        sign = -1 if x < 0 else 1
        x = abs(x)
        
        result = 0
        

        while x > 0:
            remainder = x % 10
            result = result * 10 + remainder  
            x = x // 10
        
        result *= sign
        

        if result < -2**31 or result > 2**31 - 1:
            return 0
        

        return result

# Ejemplo de uso
x = Solution()
number = -1234
print(x.reverse(number))