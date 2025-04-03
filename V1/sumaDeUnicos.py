# Dado un arreglo de enteros, debes encontrar la suma de todos los
# elementos que aparecen exactamente una vez.

# Entrada: nums = [4, 3, 2, 7, 8, 2, 3, 1]
# Salida: 20
# Explicación: Los números únicos son [4, 7, 8, 1], y su suma es 4 + 7 + 8 + 1 = 20.


nums = [4, 3, 2, 7, 8, 2, 3, 1]

def sumaUnicos(Numeros):
    # Contar la frecuencia de cada número
    contador = {}
    
    for numero in Numeros:
        if numero in contador:
            contador[numero] += 1
        else:
            contador[numero] = 1

    # Sumar solo los números que aparecen una vez
    resultado = 0
    for numero, frecuencia in contador.items():
        if frecuencia == 1:
            resultado += numero
    
    return resultado

# Ejemplo de uso
print(sumaUnicos(nums))
