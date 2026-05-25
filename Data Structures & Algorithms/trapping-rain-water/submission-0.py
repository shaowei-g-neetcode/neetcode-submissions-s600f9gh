class Solution:
    def trap(self, height: List[int]) -> int:
        # for next posistion i
        # use two pointer l, r, lMax, rMax
        # if rMax >= lMax
        # the i posistion water depend on lMax
        # so water = lMax - height[i]
        #
        # if the i hegith > lMax, lMax = height, no water
        # if lMax > rMax
        # the i water depends on rMax
        # so water = rMax - height[i]
        #
        # else rMax = height, no water
        # When to move l or r?
        # move the side with smaller current max boundary

        n = len(height)

        if n < 3: # can't trap water
            return 0

        l, r = 0, n - 1
        lMax, rMax = height[l], height[r]
        water = 0

        while l < r:
            if rMax >= lMax:
                l += 1
                lMax = max(lMax, height[l])
                water += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                water += rMax - height[r]
        
        return water
