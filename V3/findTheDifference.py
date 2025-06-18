import random
import string


class Solution(object):
    def findTheDifference(self, s:string, t:string):
        for x in t:
            if x not in s:
                return x
            s = s.replace(x,'',1)
        


String = "abc"


#Generar una secuencia random del string
shuffled_list = list(String)
random.shuffle(shuffled_list)
shuffled_string = ''.join(shuffled_list)

# Agregar una letra random
random_letter = random.choice(string.ascii_lowercase)
Added = shuffled_string + random_letter

Solucion = Solution()
print(Solucion.findTheDifference(String, Added))

# print(Added)