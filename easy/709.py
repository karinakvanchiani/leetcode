class Solution:
    def toLowerCase(self, s: str) -> str:
        return ''.join([chr(ord(char) + 32) if 65 <= ord(char) <= 90 else char for char in s])