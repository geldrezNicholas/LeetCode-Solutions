class Solution:
    def isPalindrome(self, s: str) -> bool:

        newS = ''.join(c.lower() for c in s if c.isalnum())
        left = 0
        right = len(newS) - 1

        while left < right:
            if newS[left] != newS[right]:
                return False
            left += 1
            right -= 1
        
        return True

