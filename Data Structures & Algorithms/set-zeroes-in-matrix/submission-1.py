class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROW, COL = len(matrix), len(matrix[0])

        isTopLeftZero = False

        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        isTopLeftZero = True

        for r in range(1, ROW):
            for c in range(1, COL):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROW):
                matrix[r][0] = 0

        if isTopLeftZero:
            for c in range(COL):
                matrix[0][c] = 0
        
