class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # because graph may have cycle, so we use map to save cloned nodes
        if not node:
            return None

        cloneMap = {}

        def dfs(cur: "Node"):
            if cur in cloneMap:
                return cloneMap[cur]
            
            copy = Node(cur.val)

            # save copy first to prevent cycle
            cloneMap[cur] = copy

            # copy cur neighbors
            for neighbor in cur.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        return dfs(node)