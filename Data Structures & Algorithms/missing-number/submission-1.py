class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        x = n

        for i, n in enumerate(nums):
            x ^= i ^ n
        
        return x