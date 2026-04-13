class Solution:
    def rob(self, nums: List[int]) -> int:


        pre1 = 0
        pre2 = 0

        for i in range(len(nums)):
            temp =   pre1
            pre1 = max(pre2 + nums[i], pre1)
            pre2 = temp

        return pre1       

     