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
        for key, value in hash1.items():
            if key not in hash2:
                return False
            else:
                if hash1[key] != hash2[key]:
                    return False
            
        return True

        
        