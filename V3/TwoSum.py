class Solution(object):

    def twoSum(self,Numeros, target):
       hashmap =  {}
       
       for x,y in enumerate(Numeros):
           complemento = target-y
           
           if complemento in hashmap:
               return [hashmap[complemento], x]
           
           hashmap[y] = x
        

nums = [2, 7, 11, 15]
target = 9
print(Solution.twoSum(nums, target))