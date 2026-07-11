class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        i = max(weights)
        j = sum(weights)
        res = sum(weights)
        while i <= j:
            mid = (i + j) // 2
            if self.canShip(weights, days, mid):
                res = min(res, mid)
                j = mid - 1
            else:
                i = mid + 1
        return res

    def canShip(self, weights, days, capacity):
        days_needed = 1
        curr_capacity = capacity
        for weight in weights:
            if curr_capacity - weight < 0:
                days_needed += 1
                if days_needed > days:
                    return False
                curr_capacity = capacity
            curr_capacity -= weight
        return True
        