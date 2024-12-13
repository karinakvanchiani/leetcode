class Solution:
    def frequencySort(self, s: str) -> str:
        sorted_s = sorted(set(s), key=lambda x: s.count(x), reverse=True)
        return ''.join([char * s.count(char) for char in sorted_s])