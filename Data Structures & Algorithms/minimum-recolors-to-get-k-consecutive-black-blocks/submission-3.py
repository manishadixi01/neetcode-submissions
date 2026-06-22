
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        r = k
        min_opn = len(blocks)
        while r <= len(blocks):
            curr = blocks[l : r]
            min_opn = min(curr.count('W'), min_opn)
            l += 1
            r += 1  
        return min_opn

        