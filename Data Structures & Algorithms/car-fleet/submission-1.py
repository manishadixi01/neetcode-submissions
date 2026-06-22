import math
from collections import Counter
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        steps = []
        for p,s in pair:
            time = (target - p) / s
            if steps and time <= steps[-1]:
                continue
            steps.append(time)
        return len(steps)


        

        