class StockSpanner:

    def __init__(self):
        self.stack = []
        self.idx = 1
    def next(self, price: int) -> int:
        while self.stack and price >= self.stack[-1][1]:
            self.stack.pop()
        self.stack.append((self.idx, price))
        self.idx += 1
        if len(self.stack) > 1:
            return (self.stack[-1][0] - self.stack[-2][0])
        else:
            return self.stack[-1][0]

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)