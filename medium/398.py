class Solution:

    def __init__(self, nums: List[int]):
        self.indexes = defaultdict(list)

        for i, num in enumerate(nums):
            self.indexes[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.indexes[target])