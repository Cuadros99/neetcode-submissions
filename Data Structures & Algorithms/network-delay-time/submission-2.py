class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        unvisited_nodes = set(range(1,n+1))
        heap = []
        distance_map = defaultdict(lambda: float('inf'))
        nodes_map = defaultdict(list)
        min_time = 0

        for ui, vi, ti in times:
            nodes_map[ui].append((vi, ti))

        heap.append((0, k))
        distance_map[k] = 0

        while heap:
            print(f"{heap} - {unvisited_nodes}")
            distance, node = heapq.heappop(heap)
            if node in unvisited_nodes:
                unvisited_nodes.remove(node)
            if distance > distance_map[node]:
                continue
            for vi, ti in nodes_map[node]:
                if (ti + distance) < distance_map[vi]:
                    distance_map[vi] = (ti + distance)
                    heapq.heappush(heap, (distance_map[vi], vi))
            
        
        return -1 if unvisited_nodes else max(distance_map.values())
        

        
        

