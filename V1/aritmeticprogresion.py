class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        return True


Solucion = Solution()

Numbers = [1, 100]

print(Solucion.canMakeArithmeticProgression(Numbers))

