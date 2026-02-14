class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final = ""
        c1,c2 = 0,0
        while c1 <= len(word1) or c2 <= len(word2):
            if c1 <= c2:
                final += word1[c1:c1+1]
                c1+=1
            else:
                final += word2[c2:c2+1]
                c2+=1
        if(c1 < len(word1) - 1):
            final += c1[c1:]
        elif(c2 < len(word2) - 1):
            final += c2[c2:]
        return final