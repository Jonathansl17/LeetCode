# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.

class Solution(object):
    def mergeAlternately(self,word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""

        for x in range(max(len(word1), len(word2))):
            if(x < len(word1)):
                result+= word1[x]

            if(x < len(word2)):
                result+= word2[x]

        return result
        
word1 ="abcd"
word2 = "pq"    
Solucion = Solution()
print(Solucion.mergeAlternately(word1, word2))

