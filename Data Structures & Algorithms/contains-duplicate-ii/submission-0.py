from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idx_dict = defaultdict(list)
        for i in range(len(nums)):
            idx_dict[nums[i]].append(i)
            if len(idx_dict[nums[i]]) > 1:
                if idx_dict[nums[i]][-1] - idx_dict[nums[i]][-2] <= k:
                    return True
        return False
        