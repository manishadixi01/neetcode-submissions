class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        for char in expression[::-1]:
            if stack and stack[-1] == '?':
                stack.pop()
                on_true = stack.pop()
                stack.pop()
                on_false = stack.pop()
                stack.append(on_true if char == 'T' else on_false)
            else:
                stack.append(char)
        return stack[-1]
        




        