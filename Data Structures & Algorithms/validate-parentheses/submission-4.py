class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) < 2:
            return False
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif len(stack) > 0 and ((c == ')' and stack[-1] == '(' ) or (c == ']' and stack[-1] == '[' ) or (c == '}' and stack[-1] == '{' )):
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        return False
        