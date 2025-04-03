class Solution(object):
    def average(self, salary):
        
        minval = maxval = salary[0]
        
        for i in range(len(salary)):
            if salary[i] < minval:
                minval = salary[i]
                
            elif salary[i] > maxval:
                maxval = salary[i]
              
        lista = [x for x in salary if x!= maxval and x!= minval]

        resultado = 0
        
        for x in lista:
            resultado+=x
        
        return round(resultado,5)/len(lista)
 



salario = [1000,2000,3000]

Solucion = Solution()

print(Solucion.average(salario))