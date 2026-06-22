from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = defaultdict(int)
        l, r, window_size = 0, 0, 0
        for r in range(len(s)):
            
            frequency[s[r]] += 1

            while (r - l + 1) - max(frequency.values()) > k:
                frequency[s[l]] -= 1
                l += 1
                
            window_size = max(window_size, r - l + 1)

        return window_size