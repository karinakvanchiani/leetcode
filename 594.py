class Solution:
    def findLHS(self, nums: List[int]) -> int:
        unique_nums = sorted(list(set(nums)))

        subseq_len = 0
        for i in range(len(unique_nums) - 1):
            if abs(unique_nums[i + 1] - unique_nums[i]) == 1:
                len_of_pair = nums.count(unique_nums[i]) + nums.count(unique_nums[i + 1])
                if len_of_pair > subseq_len:
                    subseq_len = len_of_pair

        return subseq_len
