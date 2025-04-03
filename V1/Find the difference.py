class Solution(object):
    def findTheDifference(self, s, t):
        for x in t:
            if x not in s:
                return x
            s = s.replace(x, '', 1)
        
Solucion = Solution()

String = "aaabcd"
Added ="abcde"

print(Solucion.findTheDifference(String, Added))