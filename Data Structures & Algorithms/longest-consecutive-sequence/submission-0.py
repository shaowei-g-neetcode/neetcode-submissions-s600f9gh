class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsMap = set(nums)
        longest = 0

        for n in nums:
            # check whether the n is start of sequence
            if n - 1 not in numsMap:
                length = 0
                while n + length in numsMap:
                    length += 1
                longest = max(longest, length)        
        
        return longest
