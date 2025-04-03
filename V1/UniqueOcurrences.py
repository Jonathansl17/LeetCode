class Solution(object):
    def uniqueOccurrences(self, arr):
        Ocurrences = {}  
        for x in arr:
            Ocurrences[x] = Ocurrences.get(x, 0) + 1

        values = list(Ocurrences.values())
        
        if len(values) == len(set(values)):
            return True
        else:
            return False

Array = [4,0,2,-5,-4]
Solucion = Solution()

print(Solucion.uniqueOccurrences(Array))