class Solution(object):
    def isAnagram(self, s, t):
        
        return sorted(s) == sorted(t)
                    
Solucion = Solution()


s1 = "aacc"
s2 = "ccac"

print(Solucion.isAnagram(s1,s2))
        