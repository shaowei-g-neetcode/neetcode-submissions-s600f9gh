# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # preorder
        data = ''
        def dfs(node):
            nonlocal data
            if node:
                data += str(len(str(node.val))) + '#' + str(node.val)
                dfs(node.left)
                dfs(node.right)
            else:
                data += '0#'
        
        dfs(root)
        return data

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        l, r = 0, 0

        def dfs():
            nonlocal l, r
            while data[r] != '#':
                r += 1
            length = int(data[l:r])
            if length == 0:
                l = r = r + 1
                return None
            
            val = int(data[r+1:r+1+length])
            node = TreeNode(val)
            l = r = r + 1 + length
            

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()

