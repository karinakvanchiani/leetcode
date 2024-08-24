class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        substring = ''

        for char in s:
            if char not in substring:
                substring += char
            else:
                if len(substring) > length:
                    length = len(substring)
                substring = substring[substring.index(char) + 1:] + char

        return max(length, len(substring))