class Solution:
    def maxDepth(self, s: str) -> int:
        depth, extra = 0, 0

        for char in s:
            if char == '(':
                extra += 1
            elif char == ')':
                if extra > depth:
                    depth = extra
                extra -= 1

        return depth