class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = defaultdict(int)
        for index,n in enumerate(nums):
            
            complement = target - n
            
            if complement in s :
                return [index, s.get(complement,0)]
            s[n] = index

        return 0



