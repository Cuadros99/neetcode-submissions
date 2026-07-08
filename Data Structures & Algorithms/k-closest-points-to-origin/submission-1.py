class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        max_heap = []
        for i, p in enumerate(points):
            distance = math.sqrt(p[0]**2 + p[1]**2)
            max_heap.append((distance, i))
        
        heapq.heapify(max_heap)

        while k > 0:
            i = heapq.heappop(max_heap)[1]
            res.append(points[i])
            k -= 1

        return res
