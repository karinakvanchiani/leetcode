class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        unique = sorted(frozenset(nums), reverse=True)
        frequencies = sorted([(num, nums.count(num)) for num in unique], key=lambda x: x[1])
        return [num[0] for num in frequencies for _ in range(num[1])]