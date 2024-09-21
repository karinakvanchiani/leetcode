class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        seq = [0, 1]

        for i in range(2, n + 1):
            seq.append(seq[i - 1] + seq[i - 2])

        return seq[-1]
    
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        a, b = 0, 1

        for i in range(2, n + 1):
            result = a + b
            a, b = b, result

        return result