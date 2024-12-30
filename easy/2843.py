class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0

        for x in range(low, high + 1):
            string = str(x)
            n = len(string) // 2

            if len(string) % 2 == 0:
                first = sum([int(digit) for digit in string[:n]])
                last = sum([int(digit) for digit in string[n:]])

                if first == last:
                    ans += 1

        return ans