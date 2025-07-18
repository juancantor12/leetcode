"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""
class Solution:
    """
    This solution works by navigating the tree on a "deep first search" way, recursively returning the current depth if we get to
    an empty node, or returning the depth of either the left or right node, depending on what one has a higher value
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_depth):
            if not node: return current_depth  # If we get to an empty node, return the current depth
            left_depth = dfs(node.left, current_depth + 1)  # calculate the depth of the left branch, updating the depth value
            right_depth = dfs(node.right, current_depth + 1)  # same for the right branch
            return max(left_depth, right_depth)  # Lastly, return whatever depth is bigger for this current subtree

        return dfs(root, 0)  # To kickstart the navigation, call the dfs method on the root starting the depth at 0