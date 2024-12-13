class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l1, l2 = s1.split(), s2.split()
        l1.extend(l2)
        result = []

        for word in set(l1):
            if l1.count(word) == 1:
                result.append(word)

        return result
