class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        if sorted(s1) != sorted(s2):
            return False

        swap = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                swap.append((s1[i], s2[i]))

            if len(swap) > 2:
                return False

        if len(swap) != 2:
            return False

        if swap[0][0] == swap[1][1] and swap[0][1] == swap[1][0]:
            return True

        return False