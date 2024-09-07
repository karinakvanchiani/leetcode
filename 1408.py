class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = []

        for word in words:
            for another in words:
                if word != another and word in another:
                    output.append(word)
                    break

        return output