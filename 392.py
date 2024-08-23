class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True 

        indx = 0

        for letter in t:
            if letter == s[indx]:
                indx += 1
            if indx == len(s):
                return True
        
        return False