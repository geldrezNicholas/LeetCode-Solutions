class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        res = []

        heapq.heapify(res)

        for i in points:
            distance = (i[0] ** 2) + (i[1] ** 2)
            heapq.heappush(res, (distance, i))
        
        return [heapq.heappop(res)[1] for n in range(k)]

        