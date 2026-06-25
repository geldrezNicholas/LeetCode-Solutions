class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        if not s:
            return

        front = 0 
        back = len(s)-1

        while front < back:
            tmp = s[front]
            s[front] = s[back]
            s[back] = tmp
            front+=1
            back-=1



        