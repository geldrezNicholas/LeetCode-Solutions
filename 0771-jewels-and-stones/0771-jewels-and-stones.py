from collections import defaultdict

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel = defaultdict(int)

        for letter in jewels:
            jewel[letter] += 1
        
        counter = 0
        for letter in stones:
            if letter in jewel:
                counter+=1
        
        return counter