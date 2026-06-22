class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash1 = {}
        hash2 = {}
        for chars in s:
            if chars in hash1:
                hash1[chars] += 1
            else:
                hash1[chars] = 1
        for chart in t:
            if chart in hash2:
                hash2[chart] += 1
            else:
                hash2[chart] = 1
            
        return hash1 == hash2

        
        