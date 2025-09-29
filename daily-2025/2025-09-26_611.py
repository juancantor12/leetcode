"""
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:
Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Example 2:
Input: nums = [4,2,3,4]
Output: 4
"""

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort() # sort the numbers so the biggest one is at the end
        count = 0 # initialize the counter
        for i in range(len(nums) - 1, -1, -1): # Iterate from the biggest number backwards
            left, right = 0, i - 1  # initialize 2 pointers, one at the start and other at the end - 1
            while left < right:  # while the pointers haven't crossed
                if nums[left] + nums[right] > nums[i]: # if the start pointer plus the end pointer are smaller than the biggest number
                    count += right - left # all pairs (end-1 plus start.... until end -2) are always less than the biggest number
                    right -= 1 # shigt the "bigger" number pointer to the left and start iterating again
                else:
                    left += 1 # the at any point the sum is not greater than the max, move the left pointer to the right and continue iterating
        return count # lastly just return the current count.