class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        found = []
        r1, r2, r3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')

        for word in words:
            setted = set(word.lower())
            if not (setted - r1 and setted - r2 and setted - r3):
                found.append(word)

        return found