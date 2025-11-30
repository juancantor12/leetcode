"""
Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.
"""
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        r = total % p
        if r == 0:
            return 0

        mp = {0: -1}
        prefix = 0
        n = len(nums)
        ans = n

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            target = (prefix - r) % p

            if target in mp:
                ans = min(ans, i - mp[target])

            mp[prefix] = i

        return ans if ans < n else -1