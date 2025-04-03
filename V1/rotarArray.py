# Entrada: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
# Salida: [5, 6, 7, 1, 2, 3, 4]
# Explicación: El arreglo se rota 3 posiciones a la derecha.


def rotar(array, numero):
    
    listaSeparada = []
    lendeArray = len(array)
    
    for x in range(-numero, 0):
        listaSeparada.append(array[x])

    Final = listaSeparada + array[0:numero+1]
    
    print(Final)


rotar([1, 2, 3, 4, 5, 6, 7],3)