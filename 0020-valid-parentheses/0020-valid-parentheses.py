class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s) == 0 or len(s) % 2 != 0):
            return False
        if(s[0] == ')' or s[0] == '}' or s[0] == ']'):
            return False

        dict = {'(':')','[':']', '{':'}' }
        stack = []
        open = dict.keys()
        for e in s:
            if e in open:
                stack.append(e)
            else:
                if len(stack) == 0 or dict.get(stack.pop()) != e:
                    return False
        if(len(stack) == 0):
            return True
        return False
