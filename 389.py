class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = {}
        for letter in s:
            if letter not in letters:
                letters[letter] = 0
            letters[letter] += 1

        for letter in t:
            if letter not in letters:
                return letter

            if letters[letter] < 1:
                return letter

            letters[letter] -= 1