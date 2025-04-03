class Solution(object):
    def strStr(self, haystack, needle):
        
        if needle == "":
            return 0
        else:
            index = haystack.find(needle)
            return index


Solucion = Solution()

Palabra = "sadbutsad"
Busqueda = "sad"

print(Solucion.strStr(Palabra,Busqueda))



