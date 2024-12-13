class Solution:
    def longestPalindrome(self, s: str) -> str:
        def maybe_longer(start, end):
            longer = s[start:end + 1]
            i = 1

            while start - i >= 0 and end + i < n:
                if s[start - i] == s[end + i] and len(s[start - i: end + i + 1]) > len(longer):
                    longer = s[start - i: end + i + 1]
                    i += 1
                else:
                    break

            return longer

        def len_of_palindrom(k):
            longest = s[0]

            for center in range(1, n):
                maybe_palindrome = s[center - 1: center + k]

                if maybe_palindrome == maybe_palindrome[::-1]:
                    longest_i = maybe_longer(center - 1, center + k - 1)

                    if len(longest_i) > len(longest):
                        longest = longest_i

            return longest


        n = len(s)
        if n == 1:
            return s

        opt_1, opt_2 = len_of_palindrom(1), len_of_palindrom(2)
        return opt_1 if len(opt_1) > len(opt_2) else opt_2
