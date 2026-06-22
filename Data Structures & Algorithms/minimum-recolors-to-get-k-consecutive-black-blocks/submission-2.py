
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        start = 0
        curr = blocks[start:start+k]
        min_opn = len(blocks)
        while start+k <= len(blocks):
            min_opn = min(curr.count('W'), min_opn)
            start+=1
            curr = blocks[start : start + k]
        return min_opn

        