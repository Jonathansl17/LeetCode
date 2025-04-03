"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]."""

class solution:
    def TwoSum(self, numbers, target):
        for indexone in range(len(numbers)):
            for indextwo in range(len(numbers)):
                
                if numbers[indexone] + numbers[indextwo] == target:
                    return [indexone,indextwo]
                
        return False
    
Solucion = solution()

Lista = [1,2,3,4,5,6,7,8,9]
Objetivo = 9

print(Solucion.TwoSum(Lista,Objetivo))
    
    