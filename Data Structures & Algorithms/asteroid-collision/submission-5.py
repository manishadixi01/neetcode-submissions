class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for a in asteroids:
            while res and a < 0 and res[-1] > 0:
                diff = a + res[-1]
                if diff > 0:
                    a = 0
                    break
                elif diff < 0:
                    res.pop()
                    continue
                else:
                    res.pop()
                    a = 0
            if a != 0:
                res.append(a)

        return res

'''
i = 0, res =[2]
i = 1, res = [2,4]
i = 2, res = [2]
'''