class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = ''

        for char in s:
            if stack and char == stack[-1]:
                stack = stack[:-1]
            else:
                stack += char

        return stack
