class Solution(object):
    @staticmethod
    def lengthOfLastWord(s):
        return  len(s.split()[-1])

sentence= "Hello World"
Solucion = Solution()
print(Solution.lengthOfLastWord(sentence))
