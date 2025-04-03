class Solution(object):
    def findDuplicate(self, nums):
        nums.sort()
        for x in range(len(nums)):
                if nums[x] == nums[x+1]:
                    return nums[x]
                

Solucion  = Solution()


Numeros = [3,2,25,5,33]
# print(Solucion.findDuplicate(Numeros))








# Ordenamiento Burbuja
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

#Ordenamiento de Selección
def selectionSort(arr):
    
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]




# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)
print("Arreglo ordenado con burbuja:", arr)

arr = [64, 34, 25, 12, 22, 11, 90]
selectionSort(arr)
print("Arreglo ordenado con selección:", arr)
            
            
            
