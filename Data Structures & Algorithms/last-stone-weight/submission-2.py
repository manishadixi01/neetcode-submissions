import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = stones
        heapq.heapify_max(maxheap)
        while(len(maxheap) >= 2):
            max1 = heapq.heappop_max(maxheap)
            max2 = heapq.heappop_max(maxheap)
            diff = abs(max1 - max2)
            if diff > 0:
                heapq.heappush_max(maxheap, diff)
        return maxheap[0] if maxheap else 0
        