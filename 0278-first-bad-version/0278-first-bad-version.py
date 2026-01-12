# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        L, H = 1, n
        sol = -1
        while L <= H:
            M = L + (H - L) // 2
            if isBadVersion(M):
                sol = M
                H = M-1
            else:
                L = M+1
        return sol