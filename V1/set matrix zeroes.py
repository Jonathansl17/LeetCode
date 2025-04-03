Matriz = [[1,1,1,1,1],
          [1,1,0,1,1],
          [0,1,1,1,1]
          ]


def x():
    
    Zeros = set()
    Posiciones = []
    Filas = []
    
    for x in range(len(Matriz)):
        
        for y in range(len(Matriz)):
            
            if Matriz[x][y] == 0:
                
                Zeros.add(y)
                Filas.append(x)
                Posiciones.append((x,y))
                
    #Matriz[x] = [0 for _ in range(len(Matriz[0]))]
    Matriz_modificada = [
    [0 if i in Zeros else valor for i, valor in enumerate(fila)]
    for fila in Matriz]
    
    
    for i in range(len(Matriz_modificada)):
        if i in Filas :
            Matriz_modificada[i] = [0 for _ in range(len(Matriz[0]))]
        
        
    print(Matriz_modificada)



x()



[[0, 1, 0, 1, 1],
 [0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0]]

[1, 2]
{0, 2}