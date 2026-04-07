class Solution:
    def maxProduct(self, nums: List[int]) -> int:
      maxProduct = nums[0]
      minProduct = nums[0]
      res = nums[0]

      for i in range(1, len(nums)):
        preMax = maxProduct
        preMin = minProduct

        n = nums[i]
        maxProduct = max(n, preMax*n, preMin*n)
        minProduct = min(n, preMax*n, preMin*n)       
        
        res = max(res, maxProduct)

      return res