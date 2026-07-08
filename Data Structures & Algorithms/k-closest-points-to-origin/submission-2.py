class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        max_heap = []
        for i, p in enumerate(points):
            distance = math.sqrt(p[0]**2 + p[1]**2)
            heapq.heappush(max_heap, (-distance, i))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        for t in max_heap:
            distance, i = t
            res.append(points[i])

        return res
