class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_of_nums = (n * (n + 1)) // 2
        return sum_of_nums - sum(nums)