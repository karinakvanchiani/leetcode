class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return [key for key, value in Counter(nums).items() if value > 1][0]