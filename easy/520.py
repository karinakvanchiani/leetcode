class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True

        if word[0].isupper() and word[1].isupper():
            upper = True
        elif word[0].isupper() and word[1].islower() or word[0].islower() and word[1].islower():
            upper = False
        else:
            return False
        
        for char in word[2:]:
            if char.isupper() != upper:
                return False

        return True
