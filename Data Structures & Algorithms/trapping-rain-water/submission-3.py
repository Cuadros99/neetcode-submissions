class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max, right_max = height[0], height[n-1]
        l, r = 0, n-1
        total_area = 0
        
        while l < r:

            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                total_area += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                total_area += right_max - height[r]

        return total_area
