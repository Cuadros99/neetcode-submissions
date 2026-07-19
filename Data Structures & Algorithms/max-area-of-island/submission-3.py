class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        max_area = 0
        area = 0

        def dfs(i, j):
            nonlocal max_area, area

            if i<0 or i == ROWS or j<0 or j==COLUMNS:
                return
            if grid[i][j] == 0:
                return
            
            grid[i][j] = 0
            area += 1
            max_area = max(max_area, area)

            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)


        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i, j)

        return max_area



#    [[1]] -> 1
#
#    [[1, 0, 1]] -> 1
#
#    [[1, 0, 1]
#     [1, 1, 0]] -> 3
#
#    [[1, 0, 1]
#     [1, 1, 1]] -> 5

#[[0,0,1,0,0,0,0,1,0,0,0,0,0]
# [0,0,0,0,0,0,0,1,1,1,0,0,0]
# [0,1,1,0,1,0,0,0,0,0,0,0,0]
# [0,1,0,0,1,1,0,0,1,0,1,0,0]
# [0,1,0,0,1,1,0,0,1,1,1,0,0]
# [0,0,0,0,0,0,0,0,0,0,1,0,0]
# [0,0,0,0,0,0,0,1,1,1,0,0,0]
# [0,0,0,0,0,0,0,1,1,0,0,0,0]]