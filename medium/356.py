class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        points = {(x, y) for x, y in points}
        avg = sum([x for x, _ in points]) / len(points)

        for x, y in points:
            if (2 * avg - x, y) not in points:
                return False
        return True
