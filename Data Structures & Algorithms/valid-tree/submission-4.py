class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        node_map = defaultdict(list)
        preorder = []
        visited = set()

        for left, right in edges:
            if left == right:
                return False
            node_map[left].append(right)
            node_map[right].append(left)

        def dfs(node, prev):
            if node in visited:
                return False
            preorder.append(node)
            visited.add(node)
            for children in node_map[node]:
                if children == prev:
                    continue
                if not dfs(children, node):
                    return False
                
            return True

        

        return dfs(0, None) and len(preorder) == n 
                







        # n = 1 -> True?
        
        # n = 2
        # [0,1] -> True

        # non linear
        # without cycles