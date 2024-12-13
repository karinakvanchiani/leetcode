class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        xs = set([point[0] for point in points])

        if len(xs) == 1:
            return True

        mn, mx = min(xs), max(xs)
        line = (mn + mx) / 2

        groups = {}

        for point in points:
            x, y = point

            if y not in groups:
                groups[y] = []

            groups[y].append(x)

        for y, xs in groups.items():
            xs = list(set(xs))

            if len(xs) == 1:
                if xs[0] != line:
                    return False

            xs.sort()
            half = len(xs) // 2

            if len(xs) % 2 != 0:
                half += 1

            for i in range(half):
                if xs[i] + abs(xs[i] - line) * 2 != xs[-i - 1]:
                    return False
        return True
