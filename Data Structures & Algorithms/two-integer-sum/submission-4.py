class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preNums = {}

        for i in range(len(nums)):
            n = nums[i]
            if n in preNums:
                return [preNums[n], i]
            minus = target - n
            preNums[minus] =  i
