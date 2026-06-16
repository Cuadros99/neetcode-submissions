class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        max_heap = []
        stack = []
        res = 1

        for i in range(n):
            time = (target - position[i])/speed[i]
            heapq.heappush(max_heap, (-position[i], time))

        first_car = heapq.heappop(max_heap)
        stack.append(first_car[1])
        for _ in range(1,n):
            if stack[-1] < max_heap[0][1]:
                stack.append(max_heap[0][1])
                res += 1
            heapq.heappop(max_heap)
        return res

    3 , 3
