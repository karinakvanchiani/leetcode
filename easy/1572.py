class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        primary = sum([mat[i][i] for i in range(n)])
        secondary = sum([mat[i][n - 1 - i] for i in range(n)])
        return primary + secondary if n % 2 == 0 else primary + secondary - mat[n // 2][n // 2]