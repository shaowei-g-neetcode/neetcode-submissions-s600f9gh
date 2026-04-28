class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = matrix
        l, r = 0, len(m)-1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                temp = m[top][l+i]
                # bottomleft -> topleft
                m[top][l+i] = m[bottom-i][l]
                # bottomright -> bottomleft
                m[bottom-i][l] = m[bottom][r-i]
                # topright -> bottomright
                m[bottom][r-i] = m[top+i][r]
                # topleft -> topright
                m[top+i][r] = temp

            l+= 1
            r -= 1