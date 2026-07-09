class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}
        for t in tasks:
            if t in counter:
                counter[t] += 1
            else:
                counter[t] = 1
        
        max_heap = [-v for v in counter.values()]

        heapq.heapify(max_heap)
        queue = deque()
        time = 0
        while max_heap or queue:
            time += 1

            if max_heap:
                remaining = 1 + heapq.heappop(max_heap)
                if remaining < 0:
                    queue.append((remaining, time + n))

            if queue and queue[0][1] == time:
                remaining, _ = queue.popleft()
                heapq.heappush(max_heap, remaining)

        return time


