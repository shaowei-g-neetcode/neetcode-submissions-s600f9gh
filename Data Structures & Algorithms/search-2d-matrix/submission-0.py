class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1

        while l <= r:
            mid = l + (r - l) // 2
            row, col = mid // n, mid % n
            item = matrix[row][col]
            if item == target:
                return True
            if item < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
