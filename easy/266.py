class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return len([val for val in Counter(s).values() if val % 2 != 0]) <= 1