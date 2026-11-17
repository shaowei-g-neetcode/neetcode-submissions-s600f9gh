class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        l = 0
        r = length - 1
        if nums[r] >= nums[l]:
            return nums[l]
        res = float('inf')


        while l < r:
            mid = l + (r - l)//2 
            res = min(res, nums[mid])

            if nums[l] > nums[r]:
                if nums[mid] > nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                r = mid - 1

        return res if res != float('inf') else 0