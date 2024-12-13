class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        substring = ''
        store = {}
        counter = 0

        for i, char in enumerate(s):
            if char not in substring:
                substring += char
                store[char] = i
            else:
                if len(substring) > length:
                    length = len(substring)
                substring = substring[store[char] + 1 - counter:] + char
                counter = store[char] + 1
                store[char] = i

        return max(length, len(substring))
    
class Solution:
    def lengthOfLongestSubstring(self, s: str, k: int) -> int:
        if not s or k < 1:
            return -1
        
        if len(s) == 1:
            return 1
        
        slow, fast = 0, 1
        seen, max_len = {}, 1
        seen[s[slow]] = 1

        while fast < len(s):
            seen[s[fast]] = seen.get(s[fast], 0) + 1

            while len(seen) > k:

                seen[s[slow]] -= 1
                if seen[s[slow]] == 0:
                    del seen[s[slow]]
                slow += 1

            max_len = max(max_len, fast - slow + 1)
            fast += 1
            
        return max_len