import random
import string


class Solution(object):
    def findTheDifference(self, s, t):
        
        for x in t:
            if x not in s:
                print(x)
                return x
            else:
                s = s.replace(x,'',1)


palabra = "abcd"
letrasRandom = string.ascii_letters
palabra_list = list(palabra)
random.shuffle(palabra_list)
palabraRandom = ''.join(palabra_list) + random.choice(letrasRandom)

Sol = Solution()
Sol.findTheDifference(palabra,palabraRandom)