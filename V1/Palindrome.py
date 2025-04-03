class Solution(object):
    def isPalindrome(self, s):
        s = "".join(letra for letra in s if letra.isalnum()).lower()
        if len(s)<=1:
            return True
        
        else:
            if s[0] == s[-1]:
                return self.isPalindrome(s[1:-1])
            
            else:
                return False
    
    
Solucion = Solution()

print(Solucion.isPalindrome("A man, a plan, a canal: Panama"))