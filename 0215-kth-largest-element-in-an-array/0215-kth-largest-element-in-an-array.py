class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums = [-n for n in nums]
        
        heapq.heapify(nums)

        for i in range(k):
            if i == k-1:
                return -heapq.heappop(nums)
            heapq.heappop(nums)