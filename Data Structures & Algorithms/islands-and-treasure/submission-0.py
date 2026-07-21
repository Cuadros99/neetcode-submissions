class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLUMNS = len(grid), len(grid[0])

        def dfs(i, j, distance):
            if i < 0 or i == ROWS or j < 0 or j == COLUMNS:
                return 
            if grid[i][j] == -1:
                return 
            if grid[i][j] == 0 and distance > 0:
                return 
            if grid[i][j] > 0 and distance >= grid[i][j]:
                return

            grid[i][j] = distance
            distance += 1

            dfs(i+1, j, distance)
            dfs(i-1, j, distance)
            dfs(i, j+1, distance)
            dfs(i, j-1, distance)


        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == 0:
                    dfs(i,j, 0)
