class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for index, n in enumerate(nums):
            
            complement = target - n
            
            if complement in s :
                return [index, s[complement]]
            s[n] = index

        return 0



