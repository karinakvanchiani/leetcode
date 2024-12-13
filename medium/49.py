class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s, t):
            if len(s) != len(t):
                return False
            
            set_s = set(s)
            return sum([True for char in set_s if s.count(char) == t.count(char)]) == len(set_s)

        anagrams = {}

        for string in strs:
            string_length = len(string)
            added = False

            if string_length not in anagrams:
                anagrams[string_length] = {}

            for key in anagrams[string_length]:
                if isAnagram(key, string):
                    anagrams[string_length][key].append(string)
                    added = True
                    break
            
            if not added:
                anagrams[string_length][string] = [string]

        return [group for length in anagrams for group in anagrams[length].values()]
    
class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())