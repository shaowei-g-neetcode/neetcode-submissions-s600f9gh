class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # topleft
                temp = matrix[top][l + i]
                # bottomleft -> topleft
                matrix[top][l+i] = matrix[bottom-i][l] 
                # bottomright -> bottomleft
                matrix[bottom-i][l] = matrix[bottom][r-i]
                # topright -> bottomright
                matrix[bottom][r-i] = matrix[top+i][r]
                # topleft -> topright
                matrix[top+i][r] = temp
                
                l += 1
                r -= 1
