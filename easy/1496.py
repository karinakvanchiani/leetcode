class Solution:
    def isPathCrossing(self, path: str) -> bool:
        points = {(0, 0)}
        x = y = 0

        for move in path:
            x += 1 if move == 'E' else (-1 if move == 'W' else 0)
            y += 1 if move == 'N' else (-1 if move == 'S' else 0)

            if (x, y) in points:
                return True

            points.add((x, y))

        return False