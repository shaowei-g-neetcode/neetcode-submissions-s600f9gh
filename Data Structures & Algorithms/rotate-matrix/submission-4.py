class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # swap top bottom
        for top in range(n//2):
            bottom = n - 1 - top
            matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
        
        # transpose
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

