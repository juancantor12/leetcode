"""
You are given a 0-indexed integer array nums.
An index i is part of a hill in nums if the closest non-equal neighbors of i are smaller than nums[i].
Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i are larger than nums[i].
Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].
Note that for an index to be part of a hill or valley, it must have a non-equal neighbor
on both the left and right of the index.
Return the number of hills and valleys in nums.
"""
class Solution:
    """
    This solution works by iterating the array once and and keeping track of what direction, either up or down
    we took on the last change of altitude, if we move up after having down in our las direction this means
    we crossed a hill, so we bumb the number and update the direction, likewise, if we moved down and our previous
    direction was up, we bump the number and change the direction to down, if the direction doesnt change (same altitude)
    we dont bump the number nor we change the previous direction
    """
    def countHillValley(self, nums: List[int]) -> int:
        hills_and_valleys = 0  # Counter
        direction = None  # Previous direction
        for i in range(1, len(nums)):  # iterate array
            if nums[i] > nums[i-1]:  # If previous tile was lower we are moving up
                if direction == "down":  # if we previously moved down, we are in a valley
                    hills_and_valleys += 1  # so we bump the counter
                direction = "up"  # and update the direction change
            elif nums[i] < nums[i-1]:  # if the previous tile was higher we are moving down
                if direction == "up":  # If we previously modev up, this means we crossed a hill
                    hills_and_valleys += 1  # so we bump the counter
                direction = "down"  # and update the new "previous" direction
        return hills_and_valleys  # lastly just return the counter
