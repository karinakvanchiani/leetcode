class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        mults = []

        for i in range(-1, -(len(num2) + 1), -1):
            mults.append(int(str(int(num1) * int(num2[i])) + '0' * (-i - 1)))

        return str(sum(mults))