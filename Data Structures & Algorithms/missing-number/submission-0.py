class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = 0

        for i, n in enumerate(nums):
            x ^= i ^ n
        
        return x