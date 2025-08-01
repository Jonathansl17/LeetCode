class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        isDecreasing = True
        isIncreasing = True
        
        # Recorremos del segundo elemento al final
        for i in range(1, len(nums)):
            # Si el anterior es mayor al actual, no es creciente
            if nums[i] < nums[i - 1]:
                isIncreasing = False
            # Si el anterior es menor al actual, no es decreciente
            if nums[i] > nums[i - 1]:
                isDecreasing = False

        # Es monótono si al menos uno es verdadero
        return isIncreasing or isDecreasing

# Ejemplos de prueba
solucion = Solution()
print(solucion.isMonotonic([1, 3, 2]))  # False
print(solucion.isMonotonic([1, 2, 2, 3]))  # True (creciente)
print(solucion.isMonotonic([5, 4, 4, 2]))  # True (decreciente)
print(solucion.isMonotonic([7, 7, 7]))  # True (ambas)

