class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_d = set(nums1)
        nums2_d = set(nums2)
        res1 = []
        res2 = []

        for i in nums1_d:
            if i not in nums2_d:
                res1.append(i)
        for i in nums2_d:
            if i not in nums1_d:
                res2.append(i)
        final_res = []
        final_res.append(res1)
        final_res.append(res2)
        return final_res