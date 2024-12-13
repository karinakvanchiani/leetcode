class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            average = (start + end) // 2

            if nums[average] == target:
                return average
            
            elif nums[average] > target:
                end = average - 1

            else:
                start = average + 1

        return -1