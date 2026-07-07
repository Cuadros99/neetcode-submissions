class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for n in nums:
            heapq.heappush(self.heap, -n)

    def add(self, val: int) -> int:
        aux = []
        heapq.heappush(self.heap, -val)
        for i in range(self.k-1):
            aux.append(- heapq.heappop(self.heap))
        res = -self.heap[0]
        for n in aux:
            heapq.heappush(self.heap, -n)
        return res