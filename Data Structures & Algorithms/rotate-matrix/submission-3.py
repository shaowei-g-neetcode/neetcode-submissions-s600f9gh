class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)
        
        # swap top bottom 
        for top in range(n//2):
            bottom = n - 1 - top
            matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
        
        # transpose
        for i in range(n):
            for j in range(i+1, n):  
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]

