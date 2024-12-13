class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        flatten = [0]

        for row in matrix:
            flatten.extend(row)

        for i in range(n):
            matrix[i] = flatten[-(n - i):0:-n]