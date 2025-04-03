Arreglo = [1, 4, 6, 4, 5, 7, 20]
target = 21

def twoSum():
    for x in range(len(Arreglo)):
        for i in range(x + 1, len(Arreglo)):
            if Arreglo[x] + Arreglo[i] == target:
                return [x, i]

print(twoSum())