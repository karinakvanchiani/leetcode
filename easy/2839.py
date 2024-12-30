class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        s1_1 = s1[2] + s1[1] + s1[0] + s1[3]
        if s1_1 == s2:
            return True

        s1_2 = s1[0] + s1[3] + s1[2] + s1[1]
        if s1_2 == s2:
            return True

        s1_2 = s1_1[0] + s1_1[3] + s1_1[2] + s1_1[1]
        if s1_2 == s2:
            return True

        return False