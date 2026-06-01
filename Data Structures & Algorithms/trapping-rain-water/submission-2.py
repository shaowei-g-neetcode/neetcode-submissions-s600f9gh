class Solution:
    def trap(self, height: List[int]) -> int:
        # use two pointer
        # l, r, maxL, maxR
        # for next i position:
        # if maxR >= maxL:
        #   water = maxL - height[l] 
        # else: 
        #   water = maxR - height[r]
        # how to move pointer?
        # move the side with smaller max boundary 

        n = len(height)
        if n < 3:
            return 0

        l, r = 0, n - 1
        lMax, rMax = height[l], height[r]
        water = 0

        while l < r:
            print(l, r)
            if rMax >= lMax:
                l += 1
                lMax = max(lMax, height[l])
                water += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                water += rMax - height[r]
        return water
