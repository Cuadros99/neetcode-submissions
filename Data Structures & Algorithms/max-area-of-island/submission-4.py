class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        max_area = 0

        def dfs(i, j):
            nonlocal max_area

            if i<0 or i == ROWS or j<0 or j==COLUMNS:
                return 0
            if grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0

            return 1 + dfs(i+1, j) + dfs(i, j+1) + dfs(i-1, j) + dfs(i, j-1)


        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

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