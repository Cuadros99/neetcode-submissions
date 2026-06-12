class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0

        while l<r:
            lenght = r-l
            if heights[l] > heights[r]:
                min_h = heights[r]
                r -= 1
            else:
                min_h = heights[l]
                l += 1

            area = min_h * lenght
            max_area = max(max_area, area)

        return max_area

