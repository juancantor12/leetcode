"""
You are given an array of n strings strs, all of the same length.
We may choose any deletion indices, and we delete all the characters in those indices for each string.
For example, if we have strs = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"].
Suppose we chose a set of deletion indices answer such that after deletions, the final array has every string (row) in lexicographic order. (i.e., (strs[0][0] <= strs[0][1] <= ... <= strs[0][strs[0].length - 1]), and (strs[1][0] <= strs[1][1] <= ... <= strs[1][strs[1].length - 1]), and so on). Return the minimum possible value of answer.length.
"""
class Solution(object):
    def minDeletionSize(self, A):
        W = len(A[0])
        dp = [1] * W
        for i in range(W-2, -1, -1):
            for j in range(i+1, W):
                if all(row[i] <= row[j] for row in A):
                    dp[i] = max(dp[i], 1 + dp[j])

        return W - max(dp)