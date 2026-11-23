# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

# The path sum of a path is the sum of the node's values in the path.

# Example 1:
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(cur):
            nonlocal res
            if not cur:
                return 0
            leftVal = max(0, dfs(cur.left))
            rightVal = max(0, dfs(cur.right))
            res = max(res, cur.val + leftVal + rightVal)
            return cur.val + max(leftVal, rightVal)

        dfs(root)

        return res


        