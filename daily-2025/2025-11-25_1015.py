"""
Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.
Return the length of n. If there is no such n, return -1.
Note: n may not fit in a 64-bit signed integer.
"""
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 1: return 1
        if k % 2 == 0 or k % 5 == 0: return -1
        remainder = 0
        for i in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0: return i
        return -1