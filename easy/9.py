class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        ans = True
        for i in range(len(s) // 2):
            if s[i] != s[-(i + 1)]:
                ans = False
        return ans