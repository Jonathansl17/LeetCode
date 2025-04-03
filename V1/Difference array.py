class Solution:
    def findDifference(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)

        diff1 = set1 - set2
        diff2 = set2 - set1

        answer = list(diff1),list(diff2)
        return list(answer)

nums1 = [1, 2, 3, 3]
nums2 = [1, 1, 2, 2]

solution = Solution()
print(solution.find_difference(nums1, nums2))