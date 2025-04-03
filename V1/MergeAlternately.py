class Solution(object):
    def mergeAlternately(self, word1, word2):
        
        Final = ""
        
        len1 = len(word1)
        len2 = len(word2)
        
        for x in range(max(len1,len2)):
            
            if x < len1:
                Final+= word1[x]
            
            if x < len2:
                Final += word2[x]
                
        return Final
            
Solucion = Solution()
print(Solucion.mergeAlternately("Hola","123456"))