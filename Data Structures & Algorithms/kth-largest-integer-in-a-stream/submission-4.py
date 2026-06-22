import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = nums
        self.k = k
        heapq.heapify(self.minheap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        print(len(self.minheap), self.k)
        if len(self.minheap) > self.k:
            
            for i in range(len(self.minheap) - self.k):
                heapq.heappop(self.minheap)
        
        return self.minheap[0]

        
