class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_chars = {letter.lower(): [] for letter in word}

        for letter in word:
            if letter == letter.lower():
                lower_chars[letter].append('lower')
            else:
                lower_chars[letter.lower()].append('upper')
        
        return sum([1 if len(set(value)) > 1 else 0 for value in lower_chars.values()])