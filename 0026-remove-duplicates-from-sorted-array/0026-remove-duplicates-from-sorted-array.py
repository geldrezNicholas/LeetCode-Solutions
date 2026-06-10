class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        j = 0
        for i in nums:
            if i not in s:
                s.add(i)
                nums[j] = i
                j+=1
        return len(s)
        