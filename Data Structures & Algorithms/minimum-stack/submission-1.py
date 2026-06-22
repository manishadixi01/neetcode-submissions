import math
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = math.inf
        self.topitem = -1

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.topitem += 1
        if val < self.min:
            self.min = val 
        

    def pop(self) -> None:
        x = self.stack.pop()
        self.topitem -= 1 if self.topitem > -1 else -1
        if x == self.min:
            self.min = min(self.stack) if self.stack else math.inf

        

    def top(self) -> int:
        return self.stack[self.topitem]

    def getMin(self) -> int:
        return self.min