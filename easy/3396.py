class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        nums = deque(nums)

        while len(nums) > 0:
            if len(set(nums)) == len(nums):
                break

            else:
                for i in range(3):
                    if nums:
                        nums.popleft()
                ans += 1

        return ans