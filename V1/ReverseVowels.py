class Solution(object):
    def reverseVowels(self, s):
        Vocales = "aeiouAEIOU"
        VocalesInvertidas = ""
        
        for letra in s:
            if letra in Vocales:
                VocalesInvertidas = letra + VocalesInvertidas
        
        PalabraMutable = list(s)
        
        VocalActual = 0
        for x in range(len(PalabraMutable)):
            if PalabraMutable[x] in Vocales:
                PalabraMutable[x] = VocalesInvertidas[VocalActual]
                VocalActual+=1 
        
        
        PalabraFinal = "".join(PalabraMutable)
        
        return PalabraFinal
        
Solucion = Solution()

Palabra = "leetcode"
print(Solucion.reverseVowels(Palabra))

# class Solution(object):
#     def reverseVowels(self, s):
#         Vocales = "aeiouAEIOU"
#         s = list(s)
#         left, right = 0, len(s) - 1
        
#         while left < right:
#             if s[left] not in Vocales:
#                 left += 1
#             elif s[right] not in Vocales:
#                 right -= 1
#             else:
#                 s[left], s[right] = s[right], s[left]
#                 left += 1
#                 right -= 1
        
#         return "".join(s)
        
# Solucion = Solution()

# Palabra = "leetcode"
# print(Solucion.reverseVowels(Palabra))