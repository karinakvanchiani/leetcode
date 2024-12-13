class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        equal = {}
        max_len = -1

        for i, char in enumerate(s):
            if char not in equal:
                equal[char] = [i]
            
            if len(equal[char]) > 1 and i > equal[char][1]:
                equal[char][1] = i
            else:
                equal[char].append(i)
                
            max_len = max(max_len, equal[char][1] - equal[char][0] - 1)

        return max_len
