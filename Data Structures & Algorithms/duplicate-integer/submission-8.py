class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = []
        for n in nums:
            if n in arr:
                return True
            arr.append(n)
        return False