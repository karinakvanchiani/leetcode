class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        counts = Counter(nums[:k])
        cur_sum = sum([key * val for key, val in counts.items()])
        max_sum = cur_sum if len(counts) >= m else 0

        for i in range(k, len(nums)):
            counts[nums[i - k]] -= 1
            if counts[nums[i - k]] == 0:
                del counts[nums[i - k]]
                
            if nums[i] not in counts:
                counts[nums[i]] = 0
            counts[nums[i]] += 1

            cur_sum = cur_sum - nums[i - k] + nums[i]

            if len(counts) >= m:
                max_sum = max(max_sum, cur_sum)

        return max_sum
