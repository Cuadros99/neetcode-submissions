class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_area = 0

        for i in range(n):
            start=i
            while stack and stack[-1][0] > heights[i]:
                h = stack.pop()
                area = h[0] * (i - h[1])
                max_area = max(area, max_area)
                start = h[1]

            stack.append((heights[i], start))

        while stack:
            h = stack.pop()
            area = h[0] * (n - h[1])
            max_area = max(area, max_area)


        
        return max_area
