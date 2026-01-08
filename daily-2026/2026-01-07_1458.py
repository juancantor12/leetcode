"""
2026-01-07_1458
Intuition
The problem asks for the maximum dot product of two non-empty subsequences. Since the order of elements must remain unchanged (subsequence property), and the optimal solution depends on optimal solutions of smaller prefixes, Dynamic Programming is the ideal approach.
For any two current numbers nums1[i] and nums2[j], we have four choices to maximize our value:
Start Fresh: Multiply nums1[i] * nums2[j] and ignore all previous history. This is necessary if previous dot products were negative.
Extend: Multiply nums1[i] * nums2[j] and add it to the max dot product calculated before these indices (dp[i-1][j-1]).
Skip nums1[i]: Ignore the current number in nums1 and carry over the max value found using nums1[0...i-1] and nums2[0...j].
Skip nums2[j]: Ignore the current number in nums2 and carry over the max value found using nums1[0...i] and nums2[0...j-1].
"""
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        # dp[i][j] stores the max dot product of subsequences 
        # using nums1[0...i] and nums2[0...j]
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                product = nums1[i] * nums2[j]
                # 1. Start fresh with just this pair
                dp[i][j] = product
                # 2. Extend the previous best (add to diagonal)
                if i > 0 and j > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + product)
                # 3. Skip nums1[i] (inherit from top)
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                # 4. Skip nums2[j] (inherit from left)
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j-1])
        return dp[n-1][m-1]