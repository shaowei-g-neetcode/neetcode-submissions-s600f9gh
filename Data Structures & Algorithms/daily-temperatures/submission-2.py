class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use monotonic stack
        # stack[i] = index
        stack = []
        n = len(temperatures)
        res = [0] * n

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                predayIdx = stack.pop()
                res[predayIdx] = i - predayIdx
            stack.append(i)
        return res
