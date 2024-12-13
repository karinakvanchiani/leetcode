class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat

        elements = [el for row in mat for el in row]
        return [elements[i:(i + c)] for i in range(0, len(elements), c)]