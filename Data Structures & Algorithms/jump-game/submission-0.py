class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0

        for i in range(len(nums)):
            if i > far:
                return False

            n = nums[i]
            far = max(far, n + i)

            if far >= len(nums)-1:
                return True
        return True