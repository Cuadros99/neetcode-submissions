"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited_map = {}
        

        def dfs(node):
            if node in visited_map:
                return visited_map[node]
            new_node = Node(node.val)
            visited_map[node] = new_node

            for neighbor in node.neighbors:
                new_neighbor = dfs(neighbor)
                new_node.neighbors.append(new_neighbor)
            
            return new_node

        if node:
            dfs(node)
        else:
            return None

        return visited_map[node]