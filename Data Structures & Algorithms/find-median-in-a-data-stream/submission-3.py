class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.middle = None

    def addNum(self, num: int) -> None:
        if self.middle is None:
            self.middle = num
            return
        
        if num <= self.middle:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -self.middle)
            self.middle = heapq.heappop(self.min_heap)
        if (len(self.max_heap) - len(self.min_heap)) > 1:
            heapq.heappush(self.min_heap, self.middle)
            self.middle = -heapq.heappop(self.max_heap)
            

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return self.middle
        else:
            return (self.middle - self.max_heap[0])/2