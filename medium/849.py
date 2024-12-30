class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        extra = [-1, -1]
        dist = 1
        idx =  0

        for i in range(len(seats)):
            if seats[i] == 0:
                if i == 0:
                    extra[0] = 0
                elif i == len(seats) - 1:
                    extra[1] = idx + 1
                idx += 1

            else:
                if extra and extra[0] == 0:
                    extra[0] = idx
                else:
                    dist = max(dist, (idx + 1) // 2)
                idx = 0

        return max(dist, max(extra))