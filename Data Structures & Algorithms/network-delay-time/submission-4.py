class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        unvisited_nodes = set(range(1,n+1))
        heap = []
        nodes_map = defaultdict(list)
        min_time = 0

        for ui, vi, ti in times:
            nodes_map[ui].append((vi, ti))

        heap.append((0, k))

        while heap:
            time, node = heapq.heappop(heap)
            if node not in unvisited_nodes:
                continue
            min_time = time
            unvisited_nodes.remove(node)
            for vi, ti in nodes_map[node]:
                heapq.heappush(heap, (ti + time, vi))
            
        
        return -1 if unvisited_nodes else min_time
        

        
        

