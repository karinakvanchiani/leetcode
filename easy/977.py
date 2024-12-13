class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = [0] * len(nums)
        left, right = 0, len(nums) - 1
        last = -1

        while left != right:
            if abs(nums[left]) >= abs(nums[right]):
                squared[last] = nums[left] ** 2
                left += 1
            else:
                squared[last] = nums[right] ** 2
                right -= 1
            last -= 1

        squared[last] = nums[left] ** 2

        return squared