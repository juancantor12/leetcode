"""
Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.
Example 1:
Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.
"""
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        cur_len = 0
        nums = [0]*k + nums + [0]*k
        for i, n in enumerate(nums):
            if i == 0 and n == 1: continue
            if n == 0:
                cur_len += 1
            elif cur_len < k: return False
            else:
                cur_len = 0
        return True