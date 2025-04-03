def EncontrarHolaRepetido(texto):
    encontrado = 0

    for x in range(len(texto) - 3):

        if texto[x] == "h" and texto[x + 1] == "o" and texto[x + 2] == "l" and texto[x + 3] == "a":
            encontrado += 1


    return "No se repite" if encontrado == 1 else "se repite"
        
    
print(EncontrarHolaRepetido("holaxdhola"))


