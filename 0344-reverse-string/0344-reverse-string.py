class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        f = 0 
        b = len(s)-1

        while f < b:
            tmp = s[f]
            s[f] = s[b]
            s[b] = tmp
            f+=1
            b-=1



        