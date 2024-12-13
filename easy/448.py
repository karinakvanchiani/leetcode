class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        return [num for num in range(1, len(nums) + 1) if num not in counts]