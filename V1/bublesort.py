def bubble_sort(arreglo):
    for numero_actual in range(len(arreglo) - 1):
        
        for numero in range(len(arreglo) - numero_actual- 1):
            
            if arreglo[numero] > arreglo[numero + 1]:
                
                NumeroTemporal = arreglo[numero]
                arreglo[numero] = arreglo[numero + 1]
                arreglo[numero + 1] = NumeroTemporal
    
# Ejemplo de uso
arreglo = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arreglo)
print("Arreglo ordenado:")
print(arreglo)