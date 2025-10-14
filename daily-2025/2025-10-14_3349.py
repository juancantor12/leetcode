"""
Given an array nums of n integers and an integer k, determine whether there exist two adjacent subarrays of length k such that both subarrays are strictly increasing. Specifically, check if there are two subarrays starting at indices a and b (a < b), where:
Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
The subarrays must be adjacent, meaning b = a + k.
Return true if it is possible to find two such subarrays, and false otherwise.
 
"""
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        previous_subarray_length, current_subarray_length = 0, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current_subarray_length += 1
            else:
                previous_subarray_length = current_subarray_length
                current_subarray_length = 1
            # Check
            if (
                current_subarray_length // 2 >= k or 
                previous_subarray_length // 2 >= k or 
                min(previous_subarray_length, current_subarray_length) >= k
            ): return True

        return False