class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP, minP = nums[0], nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]

            preMax = maxP
            preMin = minP

            maxP = max(n, preMax*n, preMin*n)
            minP = min(n, preMax*n, preMin*n)

            res = max(res, maxP)

        return res