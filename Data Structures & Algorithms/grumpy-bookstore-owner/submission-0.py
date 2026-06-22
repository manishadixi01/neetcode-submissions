class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total = 0
        window_val = 0
        curr_max = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                total += customers[i]
        for i in range(minutes):
            if grumpy[i] == 1:
                window_val += customers[i]
        curr_max = total + window_val
        for j in range(minutes, len(customers)):
            if grumpy[j] == 1:
                window_val += customers[j]
            if grumpy[j-minutes] == 1:
                window_val -= customers[j-minutes]
            curr_max = max(curr_max, total + window_val)
        return curr_max


        