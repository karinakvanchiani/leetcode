class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True

        point0, point1 = coordinates[:2]
        if point1[0] == point0[0]:
            for point in coordinates[2:]:
                if point[0] != point1[0]:
                    return False

        else:
            k = (point1[1] - point0[1]) / (point1[0] - point0[0])
            b = point0[1] - k * point0[0]

            for point in coordinates[2:]:
                if k * point[0] + b != point[1]:
                    return False

        return True