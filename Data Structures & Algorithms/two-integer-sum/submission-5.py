class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        obj = {}
        # for a num obj key = num's pair, val = num's idx
        for i in range(len(nums)):
            n = nums[i]
            pair = target - n
            if n in obj:
                return [obj[n],i]
            if pair not in obj:
                obj[pair] = i
        return []