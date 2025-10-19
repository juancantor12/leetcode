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
        nums.sort()                   # sort to handle in increasing order
        curr = float('-inf')          # next available smallest number
        ans = 0
        for x in nums:
            start, end = x - k, x + k
            pick = max(start, curr)   # smallest number >= curr
            if pick <= end:
                ans += 1
                curr = pick + 1       # move pointer forward
        return ans