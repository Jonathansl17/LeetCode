class Solution(object):
    def toLowerCase(self, s):
        
        listed = list(s)
        
        for x in range(len(s)):
            
            if listed[x].isupper():
                listed[x] = listed[x].lower()

        return "".join(listed)

Solucion = Solution()

String = "Hello"


print(Solucion.toLowerCase(String))