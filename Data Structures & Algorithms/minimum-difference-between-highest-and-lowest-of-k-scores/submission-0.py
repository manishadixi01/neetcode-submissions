class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        print(sorted_nums)
        min_diff = sorted_nums[k-1] - sorted_nums[0]
        i = 1
        while i + k <= len(sorted_nums):
                min_diff = min(min_diff, sorted_nums[i+k-1] - sorted_nums[i])
                i+=1
        return min_diff


