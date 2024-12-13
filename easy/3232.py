class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single, double = 0, 0

        for num in nums:
            if num >= 10:
                double += num
            else:
                single += num

        return double != single