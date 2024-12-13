class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        chars = set(words[0])
        result = []

        for char in chars:
            freq = min(word.count(char) for word in words)
            result += freq * [char]

        return result