# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val if root else 0

        def dfs(node):
            nonlocal res

            if not node:
                return 0

            lVal = max(0, dfs(node.left))
            rVal = max(0, dfs(node.right))

            res = max(res, node.val + lVal + rVal)

            return max(lVal, rVal) + node.val
        
        dfs(root)

        return res