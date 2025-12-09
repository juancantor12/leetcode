"""
A special triplet is defined as a triplet of indices (i, j, k) such that:
0 <= i < j < k < n, where n = nums.length
nums[i] == nums[j] * 2
nums[k] == nums[j] * 2
Return the total number of special triplets in the array.
Since the answer may be large, return it modulo 109 + 7.
"""
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        freq, prev = Counter(nums), Counter()
        cnt = 0
        prev[nums[0]] += 1
        for i in range(1, len(nums)-1):
            x = nums[i]
            x2 = x * 2
            cnt += prev[x2] * (freq[x2] - prev[x2] - (x==0))
            prev[x] += 1
        return cnt % ((10**9)+7)
