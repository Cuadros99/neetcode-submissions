class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjacency_map = defaultdict(list)

        for ui, vi, ti in times:
            adjacency_map[ui].append((vi,ti))

        heap = [(0, k)]
        visited_set = set()
        min_time = 0

        while heap and len(visited_set) < n:
            time, node = heapq.heappop(heap)
            
            if node in visited_set:
                continue

            visited_set.add(node)
            min_time = max(min_time, time)

            for neighbor, e_time in adjacency_map[node]:
                if neighbor in visited_set:
                    continue
                heapq.heappush(heap, (time + e_time, neighbor))


        return min_time if len(visited_set) == n else -1
        