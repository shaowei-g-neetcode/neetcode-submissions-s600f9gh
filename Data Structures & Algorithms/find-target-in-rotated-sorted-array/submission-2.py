class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            m = l + (r-l)//2
            print(m,nums[m],target)
            if nums[m] > target:
                if nums[l] > target:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[m] < target:
                if nums[r] > target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                return m
        
        return -1


