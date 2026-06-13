import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        win_count = {}
        res = []

        l, r = 0, 0

        while r < len(nums):

            heapq.heappush(max_heap, -nums[r])
            win_count[nums[r]] = 1 + win_count.get(nums[r], 0)
            if (r - l + 1) > k:
                if -max_heap[0] == nums[l]:
                    heapq.heappop(max_heap)
                win_count[nums[l]] -= 1
                l += 1

            if (r - l + 1) == k:
                while win_count[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                res.append(-max_heap[0])
            
            r += 1

        return res
            