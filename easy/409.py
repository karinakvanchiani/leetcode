class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1

        values = Counter(s).values()
        counts = 0
        extra = False

        for value in values:
            if value % 2 == 0:
                counts += value

            else:
                if value != 1:
                    counts += value // 2 * 2
                extra = True

        return counts + int(extra)