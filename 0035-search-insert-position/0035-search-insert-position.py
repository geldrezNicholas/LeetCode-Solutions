class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #left, right, mid
        left = 0
        right = len(nums)-1

        #edge cases
        if target > nums[right]:
            return right + 1
        elif target < nums[left]:
            return 0

        #binary search
        while left <= right:
            mid = left + (right - left) // 2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1

        return left        
                


        