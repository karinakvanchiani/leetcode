class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)

        for num in nums:
            output[num - 1] += 1

        return [i + 1 for i in range(len(output)) if output[i] == 2]