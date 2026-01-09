from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        stack = deque()
        brackets = {')': '(', ']':'[', '}': '{'}
        for para in s:
            if(para == '(' or para == '[' or para == '{'):
                stack.append(para)
            elif(para == ')' or para == ']' or para == '}'):
                if len(stack) == 0 or brackets[para] != stack.pop():
                    return False
        if len(stack) != 0:
            return False
        return True