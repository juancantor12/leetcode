"""
There are n cars on an infinitely long road. The cars are numbered from 0 to n - 1 from left to right and each car is present at a unique point.
You are given a 0-indexed string directions of length n. directions[i] can be either 'L', 'R', or 'S' denoting whether the ith car is moving towards the left, towards the right, or staying at its current point respectively. Each moving car has the same speed.
The number of collisions can be calculated as follows:
When two cars moving in opposite directions collide with each other, the number of collisions increases by 2.
When a moving car collides with a stationary car, the number of collisions increases by 1.
After a collision, the cars involved can no longer move and will stay at the point where they collided. Other than that, cars cannot change their state or direction of motion.
Return the total number of collisions that will happen on the road.
"""
class Solution:
    def countCollisions(self, directions: str) -> int:
        l, r = 0, len(directions) - 1
        # 1. Skip cars moving left on the far left (they never collide)
        while l <= r and directions[l] == 'L':
            l += 1
        # 2. Skip cars moving right on the far right (they never collide)
        while r >= l and directions[r] == 'R':
            r -= 1
        count = 0
        # 3. Any moving car (L or R) remaining in the middle will collide
        for i in range(l, r + 1):
            if directions[i] != 'S':
                count += 1
        return count