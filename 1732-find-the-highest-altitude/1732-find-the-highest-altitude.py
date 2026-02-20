class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max = 0
        current = 0
        for x in gain:
            if current + x > max:
                max = current + x
            current = current + x
        return max
