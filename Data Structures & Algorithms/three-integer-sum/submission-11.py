class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # i + j + k = 0, j + k = -i
        for i in range(len(nums)):
            # remove dulplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            num = nums[i]
            j , k = i + 1, len(nums)-1
            
            
            while j < k:
                threeSum = num + nums[j] + nums[k]
                if threeSum > 0:
                    k -= 1
                elif threeSum < 0:
                    j += 1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    k -= 1
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1

        return res
