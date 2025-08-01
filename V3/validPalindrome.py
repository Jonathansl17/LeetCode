class Solution(object):
    def isPalindrome(self, s):
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]

# Prueba del código
solucion = Solution()
string = "A man, a plan, a canal: Panama"
resultado = solucion.isPalindrome(string)
print(resultado)