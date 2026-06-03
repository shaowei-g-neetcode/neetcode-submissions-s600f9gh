from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use monotonic stack
        # stack saves day indices whose answers are not found yet
        # current day can resolve previous days' answers

        stack = []
        n = len(temperatures)
        anwser = [0] * n

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                predayIdx = stack.pop()
                anwser[predayIdx] = i - predayIdx

            stack.append(i)

        return anwser