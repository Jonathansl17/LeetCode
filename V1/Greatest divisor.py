class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if len(str1) < len(str2):
            str1, str2 = str2, str1  # Asegurarse de que str1 no es más corta que str2
        if str1[:len(str2)] != str2:  # Si str1 comienza con str2
            return ""  # No hay solución posible
        elif str2 == "":
            return str1  # El máximo divisor común de una cadena y una cadena vacía es la cadena misma
        else:
            return self.gcdOfStrings(str1[len(str2):], str2)  # Aplicar el algoritmo de Euclides
        

Solucion = Solution()
print(Solucion.gcdOfStrings("ABCABC", "ABC"))