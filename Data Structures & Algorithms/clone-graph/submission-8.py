  if not node:
            return None

        cloneMap = {}

        def dfs(cur):
            if cur in cloneMap:
                return cloneMap[cur]
            copy = Node(cur.val)
            cloneMap[cur] = copy

            for nei in cur.neighbors:
                copy.neighbors.append(dfs(nei)) 
            return copy
        
        return dfs(node)