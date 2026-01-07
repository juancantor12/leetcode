# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
2026-01-06_1339
iven the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.
Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.
Note that you need to maximize the answer before taking the mod and not after taking it.
"""
class Solution:
    ans = float("-inf")
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return 0
            return node.val + dfs(node.left) + dfs(node.right)
        total_sum = dfs(root)
        def dfs2(node):
            if not node: return 0
            subtree_sum = node.val + dfs2(node.left) + dfs2(node.right)
            self.ans = max(self.ans, (total_sum - subtree_sum) * subtree_sum)
            return subtree_sum
        dfs2(root)
        return self.ans % (10**9 + 7)
