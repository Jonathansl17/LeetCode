def Palindromo(palabra):
    palabra = palabra.lower()
    low = 0
    high = len(palabra) - 1

    while low < high:
        if palabra[low] == palabra[high]:
            low += 1
            high -= 1
        else:
            print("No es palindromo")
            return False

    print("Palindromo")
    return True


Palindromo("RADAt")