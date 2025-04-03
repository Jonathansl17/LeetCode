class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        totales = n
        flowerbed = [0] + flowerbed + [0]  

        for x in range(1, len(flowerbed)-1):
            if flowerbed[x-1] == 0 and flowerbed[x] == 0 and flowerbed[x+1] == 0:
                flowerbed[x] = 1  
                totales -= 1  
                if totales == 0:  
                    return True

        return totales <= 0 

    
Solucion = Solution()


flores = [1,0,0,0,1,0,0]
poner = 2

print(Solucion.canPlaceFlowers(flores,poner))