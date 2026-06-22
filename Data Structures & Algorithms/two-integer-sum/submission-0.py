class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetdict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] not in targetdict:
                targetdict[diff] = i
            else:
                
                return [targetdict[nums[i]], i]