class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)

        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    if i - 2 >= 0:
                        dp[i] = dp[i - 2]
                    dp[i] += 2

                else:
                    print(i, s[i], i - dp[i - 1] - 2, dp[i - dp[i - 1] - 2])
                    if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                        print(s[i - dp[i - 1] - 1])
                        if i - dp[i - 1] - 2 >= 0:
                            dp[i] = dp[i - dp[i - 1] - 2]
                        dp[i] = dp[i] + dp[i - 1] + 2

            print(i, s[i], dp[i])

        return max(dp) if dp else 0
    
sol = Solution()
print(sol.longestValidParentheses('()(())'))