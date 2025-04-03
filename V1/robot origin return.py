class Solution(object):
    def judgeCircle(self, moves):

        origin = [0,0]
        
        for x in moves:
            if x =="U":
                origin[0] +=1

            elif x == "D":
                origin[0] -=1
            
            elif x == "R":
                origin[1] +=1
            
            elif x == "L":
                origin[1]-=1 
            
        return True if origin == [0,0] else False
        
                
            

Solucion = Solution()


movements = "UD"

print(Solucion.judgeCircle(movements))
