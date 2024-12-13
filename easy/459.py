class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        substring = ''

        for letter in s[:len(s) // 2 + 1]:
            substring += letter
            repeats = len(s) // len(substring)

            if repeats != 1 and substring * repeats == s:
                return True

        return False 