class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = ""
        for char in path + '/':
            if char == '/':
                if curr == '.':
                    curr = ""
                    continue
                elif curr == '..':
                    if stack:
                        stack.pop()
                    curr = ""
                    continue
                stack.append(curr) if curr else None
                curr = ""
            else:
                curr += char

        return '/' + '/'.join(stack)
