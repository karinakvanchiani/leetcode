class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        just_a_list = [0] * 501

        for num in nums:
            just_a_list[num] += 1

        for value in just_a_list:
            if value % 2 != 0:
                return False

        return True