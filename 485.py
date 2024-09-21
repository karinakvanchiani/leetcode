class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_seq = 0
        left, right = 0, 0

        for i in range(len(nums)):
            if nums[i] == 1:
                right += 1
            else:
                if max_seq < right - left:
                    max_seq = right - left
                left, right = i + 1, i + 1

        if max_seq < right - left:
            max_seq = right - left
                
        return max_seq