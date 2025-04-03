class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        Array3 = nums1+nums2
        Array3.sort()
        
        if(len(Array3)%2==0):
            return (float(Array3[(len(Array3)-1)//2]) + float(Array3[((len(Array3)-1)//2)+1]))/2
        else:
            return Array3[len(Array3)//2]
        
Solucion  = Solution()


Array1 = [1,2]
Array2 = [3,4]

print(Solucion.findMedianSortedArrays(Array1,Array2))

