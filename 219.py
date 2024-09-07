class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_set = {}

        for i, value in enumerate(nums):
            if value in hash_set and abs(i - hash_set[value]) <= k:
                return True
            hash_set[value] = i

        return False