class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # use increasing monotonic stack
        # to calculate i heights max area, extend it's left and right boundary until find shorter height
        # add right sentry to pop all item and left sentry to prevent stack[-1] err
        heights = [0] + heights + [0]
        stack = [0]
        res = 0

        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                mid = stack.pop()            
                left = stack[-1]
                right = i
                width = right - left - 1 # should not include left and right
                area = width * heights[mid]
                res = max(res, area)                 
            stack.append(i)
        return res
