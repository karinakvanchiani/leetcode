class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for i, num in enumerate(nums):
            if target - num not in store:
                store[num] = i
            else:
                return [store[target - num], i]