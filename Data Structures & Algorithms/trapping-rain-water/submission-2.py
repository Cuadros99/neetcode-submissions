class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, 1
        total_area = 0
        cum_neg_area = [0]*len(height)
        h_map = {}
        
        while j < len(height):
            
            if height[i] > height[j]:
                cum_neg_area[j] = cum_neg_area[j-1] + height[j]
                h_map[j] = height[j]
                j += 1
            else:
                total_area += height[i]*(j-i-1) - cum_neg_area[j-1]
                cum_neg_area = [0]*len(height)
                h_map = {}
                i = j
                j += 1

            if j == len(height) and len(h_map)>0:
                remain_bars = sorted(h_map, key=h_map.get)
                k = remain_bars.pop()
                total_area += height[k]*(k-i-1) - cum_neg_area[k-1]
                cum_neg_area = [0]*len(height)
                h_map = {}
                i = k
                j = k+1

        return total_area 
            

