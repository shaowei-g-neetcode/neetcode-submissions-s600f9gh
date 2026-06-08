class Solution:
    def trap(self, height: List[int]) -> int:
        # use two pointers to calc water
        # vars: l, r, lMax, rMax
        # for next right i posistion
        # if rMax >= lMax
        # it's water deside by lMax
        # water = height[l] - lMax
        # else
        # water = height[r] - rMax
        # how to move pointers?
        # Move the side with smarller max boundary
        n = len(height)
        if n < 3:
            return 0
        l, r = 0, n - 1
        lMax, rMax = height[l], height[r]
        water = 0

        while l < r:
            if rMax >= lMax:
                l += 1
                lMax = max(lMax, height[l]) 
                water += lMax  - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                water += rMax - height[r]

        return water    
