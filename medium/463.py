class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j] == 1:
                    connect = 4

                    if i > 0:
                        connect -= 2 * grid[i - 1][j]

                    if j > 0:
                        connect -= 2 * grid[i][j - 1]

                    ans += connect
        return ans