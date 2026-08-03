from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        hash_trust = defaultdict(int)

        for [i,j] in trust:
            hash_trust[j] += 1
            hash_trust[i] -= 1
        
        for key, val in hash_trust.items():
            if hash_trust[key] == n-1:
                return key
        return -1



            

        