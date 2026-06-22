class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}
        for i in nums:
            if i not in duplicates.keys():
                duplicates[i] = 1
            else:
                return True
        return False
        