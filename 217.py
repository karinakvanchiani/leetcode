class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = set()
        for value in nums:
            if value in hash_map:
                return True
            hash_map.add(value)
        return False