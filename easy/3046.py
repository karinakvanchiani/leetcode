class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counts = {}

        for i in nums:
            if i not in counts:
                counts[i] = 0
            counts[i] += 1
            
            if counts[i] > 2:
                return False

        return True
