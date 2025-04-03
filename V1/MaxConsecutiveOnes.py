class Solution:
    def MaxConsecutiveOnes(self,BinaryList):
        MaxConsecutive= 0        
        Actual = 0

        for x in BinaryList:
            if x == 1:
                Actual+=1
                if Actual>MaxConsecutive:
                    MaxConsecutive = Actual
            else:
                Actual= 0
                
        return MaxConsecutive
    

ListaBinaria = [1,1,0,1,1,1,1,0,0,1,1,1,1,1]
Solucion = Solution()
print(Solucion.MaxConsecutiveOnes(ListaBinaria))