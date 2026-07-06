class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # calc every car time = (target-pos)/speed
        # sort car by position in descending: closet to the target
        # if current car need more time then the fleet ahead
        # it cannot catch up the fleet, so it forms a new fleet

        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        stack = []

        for pos, speed in cars:
            time = (target - pos)/speed

            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)

        