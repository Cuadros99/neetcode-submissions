class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        ROWS, COLUMNS = len(grid), len(grid[0])
        num_isl = 0

        def backtrack(i, j):
            if i<0 or i==ROWS or j<0 or j==COLUMNS:
                return
            
            if grid[i][j] == "1":
                grid[i][j] = "0"
                backtrack(i+1, j)
                backtrack(i-1, j)
                backtrack(i, j+1)
                backtrack(i, j-1)

        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == "1":
                    num_isl += 1
                    backtrack(i,j)
        return num_isl

    #   O(r*c)
        