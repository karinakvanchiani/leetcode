class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        answer = []
        nums.sort()

        while len(nums) // 2 != 1:
            answer.append((nums[-1] + nums[0]) / 2)
            nums = nums[1:-1]

        answer.append((nums[-1] + nums[0]) / 2)
        return min(answer)
