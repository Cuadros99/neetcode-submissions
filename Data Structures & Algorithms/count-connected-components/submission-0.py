class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        conected_comp = 0
        visited = set()
        nodes_map = defaultdict(list)

        for left, right in edges:
            nodes_map[left].append(right)
            nodes_map[right].append(left)


        def dfs(node):
            visited.add(node)

            for neighbor in nodes_map[node]:
                if neighbor in visited:
                    continue
                dfs(neighbor)

        for node in range(n):
            if node not in visited:
                conected_comp += 1
                dfs(node)

        return conected_comp