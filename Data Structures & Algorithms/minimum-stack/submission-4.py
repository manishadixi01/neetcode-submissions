import math
class MinStack:

    def __init__(self):
        self.stack = []
        self.topitem = -1

    def push(self, val: int) -> None:
        minval = min(val, self.stack[self.topitem][1] if self.stack else val)
        self.topitem += 1
        self.stack.append((val, minval))
        print(self.stack)
        
    def pop(self) -> None:
        x = self.stack.pop()
        self.topitem -= 1 if self.topitem > -1 else -1
        
    def top(self) -> int:
        return self.stack[self.topitem][0]

    def getMin(self) -> int:
        return self.stack[self.topitem][1]