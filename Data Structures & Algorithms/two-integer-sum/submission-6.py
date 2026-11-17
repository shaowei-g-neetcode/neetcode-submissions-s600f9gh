class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resMap = defaultdict(int)

        for i, num in enumerate(nums):
            if num in resMap:
                return [resMap[num], i]
            resMap[target - num] = i
            