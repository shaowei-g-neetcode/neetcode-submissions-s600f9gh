class Solution:
    def maxProduct(self, nums: List[int]) -> int:
      maxP = nums[0]
      minP = nums[0]
      ans = nums[0]

      for i in range(1, len(nums)):
        n = nums[i]
        
        preMax = maxP
        preMin = minP

        maxP = max(n, preMax * n, preMin * n)
        minP = min(n, preMax * n, preMin * n)
        ans = max(ans, maxP)

      return ans