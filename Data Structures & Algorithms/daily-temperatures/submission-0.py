class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        temp_stack = []
        for i in range(len(temperatures)):
            curr_temp = temperatures[i]
            while temp_stack and curr_temp > temperatures[temp_stack[-1]]:
                idx = temp_stack.pop()
                res[idx] = i - idx
            temp_stack.append(i)
        return res