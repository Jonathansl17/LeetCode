class Solution(object):
    def isAnagram(self, s, t):
        if(len(s)  != len(t)):
            return False
            
            
        ListedS = list(s)
        ListedT = list(t)
        
        for x in range(len(ListedS)):
            for j in range(x+1,len(ListedT)):
                
                if(ListedS[x] > ListedS[j]):
                    
                    ListedS[x],ListedS[j] = ListedS[j],ListedS[x]
                    
                if(ListedT[x] > ListedT[j]):
                    
                    ListedT[x],ListedT[j] = ListedT[j],ListedT[x]
                    
                    
        
        return "".join(ListedS) == "".join(ListedT)
            
        
                    
                    

Sol =Solution()

s = "anagram" 
t = "nagaram"

print(Sol.isAnagram(s,t))