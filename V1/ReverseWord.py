class Solution(object):
    def reverseWords(self, s):
        s.strip()
        
        NewWord = s.split()
        
        Final = reversed(NewWord)
        
        Result = " ".join(Final)
        return Result



Solucion = Solution()

String = "the sky is blue"

print(Solucion.reverseWords(String))