class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        res.append(asteroids[0])
        for i in range(1, len(asteroids)):
            flag_push = 1
            if res and res[-1] > 0 and asteroids[i] < 0:
                while res and abs(asteroids[i]) >= res[-1]:
                    if asteroids[i] * res[-1] > 0:
                        break
                    elif abs(asteroids[i]) == res[-1]:
                        res.pop()
                        flag_push = 0
                        break
                    else:
                        res.pop()
                if res and abs(asteroids[i]) < res[-1]:
                    flag_push = 0
            res.append(asteroids[i]) if flag_push == 1 else None     
        return res

'''
i = 0, res =[2]
i = 1, res = [2,4]
i = 2, res = [2]
'''