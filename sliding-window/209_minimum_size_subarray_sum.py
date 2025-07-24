"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1
"""
class Solution:
    """
    This solution works by sliding a window through the array, increasing it to the right when its sum is not enough
    and decreasing it from the left when the sum is over the target, at every resizal, if the sum is equal or greater
    than the target, a new "minimum" subarray lenght is calculated.
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0  # Left side of the window
        r = 0  # right side of the window
        current_window_size = 0  # Current window size
        min_window_size = float("inf")  # Minimum lenght
        current_sum = 0  # cum of the current window
        while r < len(nums):  # while the right value is within bounds
            current_window_size += 1  # Expand the window to the right
            current_sum += nums[r]  # Add the expanded entry to the current sum
            if current_sum >= target:  # If the current sum meets the target, try to decrease the window from the left
                min_window_size = min(min_window_size, current_window_size)  # Since thi window has a valid sum, update the min window size
                while current_sum >= target: # now, while the current sum still meets the target, start decreasing it
                    current_sum -= nums[l]  # decrease the value of the current sum by the amount of the left pointer
                    current_window_size -= 1  # decrease the window size
                    l += 1  # and move the left pointer to the right
                    if current_sum >= target:  # if after this decrease the sum stil holds...
                        min_window_size = min(min_window_size, current_window_size)  # update the min and continue to next shrinking attempt
            r += 1  # After the window shrink attemps end, signal increaste to the right
        return min_window_size if min_window_size != float("inf") else 0  # lastly returns the min size if is not inf, if so, return 0
