class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_length = len(p)
        sorted_p = ''.join(sorted(p))
        starts = []
        start = 0

        while start < len(s) - p_length + 1:

            if ''.join(sorted(s[start:start + p_length])) == sorted_p:
                starts.append(start)
                start += 1

            else:
                if s[start + p_length - 1] not in p:
                    start += p_length
                else:
                    start += 1

        return starts