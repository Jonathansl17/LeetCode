""""

"""
class Solution(object):
    def merge(self, nums1,n, nums2,m):
        
        m = len(nums1)
        n = len(nums2)
        FinalList = []
        for x,y in zip(nums1,nums2):
            if x == 0:
                pass
            
            else:
                FinalList.append(x)
                FinalList.append(y)
                    
        nums1 = FinalList
        print(nums1)

One = [1,2,3,0,0,0]
Two = [2,5,6]

Solucion = Solution()

Solucion.merge(One,3,Two,3)

                
    