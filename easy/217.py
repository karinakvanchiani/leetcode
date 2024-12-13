class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for value in nums:
            if value in hash_set:
                return True
            hash_set.add(value)
        return False