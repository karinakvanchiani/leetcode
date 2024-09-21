class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        if len(position) == 1:
            return 0

        even = len([pos for pos in position if pos % 2 == 0])

        return min(even, len(position) - even)