class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = target - nums[i]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == d[nums[i]]:
                    return [i, j]