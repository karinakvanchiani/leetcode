class Solution:
    def isValid(self, s: str) -> bool:
        opens = ['(', '{', '[']
        open_to_close = {'(': ')', '[': ']', '{': '}'}
        
        i = 0
        while len(s) > 1 and i < len(s) - 1:
            if s[i] in opens and s[i + 1] == open_to_close[s[i]]:
                s = s[:i] + s[i + 2:]   
                i = 0
            else:
                i += 1

        if len(s) == 0:
            return True
        
        return False