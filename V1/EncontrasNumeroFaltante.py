# Entrada: nums = [3, 0, 1]
# Salida: 2
# Explicación: El número 2 falta en el arreglo, ya que tenemos todos los números del 0 al 3 excepto el 2.


Numeros = [0, 1, 0, 3, 12]


def EncontrarFaltante(numeros):


    for x in range(len(numeros)):
        
        for j in range(x+1,len(numeros)):
            
            if numeros[x] > numeros[j]:
                
                numeros[x],numeros[j] = numeros[j], numeros[x]
    
    
    for x  in numeros:
        if x == 0:
            numeros.append(0)
            numeros.pop(x)
    
    print(numeros)
    
EncontrarFaltante(Numeros)


# Entrada: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
# Salida: [5, 6, 7, 1, 2, 3, 4]
# Explicación: El arreglo se rota 3 posiciones a la derecha.
