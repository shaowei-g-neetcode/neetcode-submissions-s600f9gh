class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsMap = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in numsMap:
                length = 0
                while n + length in numsMap:
                    length += 1
                res = max(res, length)

        return res