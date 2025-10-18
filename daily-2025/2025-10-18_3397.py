"""
You are given an integer array nums and an integer k.
You are allowed to perform the following operation on each element of the array at most once:
Add an integer in the range [-k, k] to the element.
Return the maximum possible number of distinct elements in nums after performing the operations.
Example 1:
Input: nums = [1,2,2,3,3,4], k = 2
Output: 6
Explanation:
nums changes to [-1, 0, 1, 2, 3, 4] after performing operations on the first four elements.
"""
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        nums.sort()
        count = 0
        prev = -(1 << 30)
        for a in nums:
            low = a - k
            high = a + k
            x = prev + 1
            if x < low:
                x = low
            if x <= high:
                count += 1
                prev = x
        return count