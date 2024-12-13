class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        parts = ''.join([str(num) for num in nums]).split('0')
        lengths = [len(part) for part in parts]

        if len(lengths) == 1 and lengths[0] == len(nums):
            return len(nums) - 1

        max_length = 0
        for i in range(len(lengths) - 1):
            if lengths[i] + lengths[i + 1] > max_length:
                max_length = lengths[i] + lengths[i + 1]

        return max_length