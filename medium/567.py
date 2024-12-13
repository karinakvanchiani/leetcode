class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_s1 = {chr(i): s1.count(chr(i)) for i in range(97, 123)}
        hash_sub = {chr(i): s2[:len(s1)].count(chr(i)) for i in range(97, 123)}
        i = 0
        
        while i < len(s2) - len(s1) and hash_s1 != hash_sub:
            hash_sub[s2[i]] -= 1
            i += 1
            hash_sub[s2[i + len(s1) - 1]] += 1

        return hash_s1 == hash_sub