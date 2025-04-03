class Solution(object):
    def lengthOfLastWord(self, s):
        counter = 0
 
        for x in range(len(s)-1,-1,-1):
            
            if s[x] == " " and counter ==0:
                pass
        
            elif s[x] != " ":
                counter +=1
            
            else:
                return counter
        return counter
             
             
          
            
Solucion = Solution()

print(Solucion.lengthOfLastWord("a    "))