class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        Records = []

        for x in range(len(operations)):
            if operations[x].lstrip('-').isdigit():
                Records.append(int(operations[x]))

            elif operations[x] == "+":
                Records.append(Records[-1] + Records[-2])

            elif operations[x] == "C":
                Records.pop()

            else:
                Records.append(Records[-1] * 2 )

        return (sum(Records))



ops = ["5","-2","4","C","D","9","+","+"]
Solucion = Solution()
print(Solucion.calPoints(ops))