class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        set_s = set(s)
        return sum([True for char in set_s if s.count(char) == t.count(char)]) == len(set_s)