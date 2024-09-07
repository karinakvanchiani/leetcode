class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        reversed_string = ''
        reversed_alphas = ''

        for char in s[::-1]:
            if char.isalpha():
                reversed_alphas += char
        
        for char in s:
            if char.isalpha():
                reversed_string += reversed_alphas[0]
                reversed_alphas = reversed_alphas[1:]
            else:
                reversed_string += char

        return reversed_string
