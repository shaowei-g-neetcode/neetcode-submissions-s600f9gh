class Solution:
    def trap(self, height: List[int]) -> int:
        # use two pointer to calc water
        # defind l, r , lMax, rMax
        # if rMax >= lMax:
        #   for l pointer's next position    
        #   water depends on lMax height
        #   if height[l] > lMax, water = 0
        #
        # else:
        #   for r pointers next position
        #   water depends on rMax hegith
        #   if height[r] > rMax, water = 0
        #
        # How to move pointers?
        # move the side with smaller max height boundary
        n = len(height)
        if n < 3:
            return 0

        l, r, = 0, n - 1
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