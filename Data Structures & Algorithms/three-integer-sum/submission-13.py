class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n-2):
            j= i + 1
            k = n - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    k -= 1
                    j += 1
                    while nums[k] == nums[k+1] and j < k:
                        k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1
                    

        
        return res
            
