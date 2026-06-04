class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use monotonic stack to save temp from bigger to smaller
        # for i day
        # i day can resolve previous day's answer
        n = len(temperatures)
        stack = []
        res = [0] * n


        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                predayIdx = stack.pop()
                res[predayIdx] = i - predayIdx
            stack.append(i)

        return res