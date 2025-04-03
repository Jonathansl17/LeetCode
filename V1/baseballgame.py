class Solution(object):
    def calPoints(self, operations):
        
        def is_int(n):
            try:
                int(n)
                return True
            except ValueError:
                return False

        converted = [int(x) if is_int(x) else str(x) for x in operations]

        record = []
        
        for x in range(len(converted)):
            
            if converted[x] == "C":
                record.pop()
            
            elif converted[x]  == "D":
                record.append(record[-1]*2)
            
            elif converted[x]  == "+":
                if len(record) >= 2:
                    record.append(record[-2]+ record[-1])

            else:
                if type(converted[x]) == int:
                    record.append(converted[x])
                
        return sum(record)
            

        
Solucion = Solution()


ops = ["5","-2","4","C","D","9","+","+"]
print(Solucion.calPoints(ops))