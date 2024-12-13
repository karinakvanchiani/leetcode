class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)

        skipped, repeated = -1, -1
        num = 1

        while skipped == -1 or repeated == -1:
            if num not in counts:
                skipped = num
                
            elif counts[num] == 2:
                repeated = num

            num += 1

        return [repeated, skipped]