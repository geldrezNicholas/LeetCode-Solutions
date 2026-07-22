class Solution:
    def reverseVowels(self, s: str) -> str:
        front = 0
        back = len(s)-1
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])
        l = list(s)

        while front < back:
            if l[front] in vowels and l[back] in vowels:
                tmp = l[front]
                l[front] = l[back]
                l[back] = tmp
                front += 1
                back -= 1
            elif l[front] in vowels and l[back] not in vowels:
                back -= 1
            elif l[front] not in vowels and l[back] in vowels:
                front +=1
            else:
                front +=1
                back -=1
        return ''.join(l)