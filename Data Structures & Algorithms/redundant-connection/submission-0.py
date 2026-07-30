class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.nodes_map = defaultdict(set)
        self.edges = edges

        for l, r in edges:
            self.nodes_map[l].add(r)
            self.nodes_map[r].add(l)

        for i in range(len(edges)-1, -1, -1):
            if self.checkConnectedUncycled(edges[i]):
                return edges[i]

    
    def checkConnectedUncycled(self, removed_edge):
        visited, cycle = set(), set()
        
        def dfs(node, prev):
            if node in cycle:
                return False

            visited.add(node)
            cycle.add(node)

            for neighbor in self.nodes_map[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False
            
            cycle.remove(node)
            return True
        
        left_node, right_node = removed_edge
        self.nodes_map[left_node].remove(right_node)
        self.nodes_map[right_node].remove(left_node)

        output = dfs(1, None) and (len(visited) == len(self.edges))

        self.nodes_map[left_node].add(right_node)
        self.nodes_map[right_node].add(left_node)

        return output




