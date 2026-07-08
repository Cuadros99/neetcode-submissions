class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for i, p in enumerate(points):
            distance = math.sqrt(p[0]**2 + p[1]**2)
            max_heap.append((-distance, i))
        
        heapq.heapify(max_heap)

        while max_heap and len(max_heap) > k:
            heapq.heappop(max_heap)

        return [points[i[1]] for i in max_heap]
