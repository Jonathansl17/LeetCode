# Ordenamiento Burbuja
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
  

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
            
            
            