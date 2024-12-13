class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min([sum([int(dig) for dig in str(num)]) for num in nums])