class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum, digit_sum = 0, 0
        
        for num in nums:
            digit_sum += sum([int(digit) for digit in str(num)])
            element_sum += num

        return abs(element_sum - digit_sum)