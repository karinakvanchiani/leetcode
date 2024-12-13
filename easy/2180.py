class Solution:
    def countEven(self, num: int) -> int:
        return len([number for number in range(1, num + 1) if sum([int(digit) for digit in str(number)]) % 2 == 0])