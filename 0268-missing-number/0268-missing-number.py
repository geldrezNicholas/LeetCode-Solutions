class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums) + 1
        total = 0
        for i in range(size):
            total += i
        
        numstotal = 0
        for n in nums:
            numstotal+=n
        
        return total - numstotal