class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLUMNS = len(grid), len(grid[0])
        spaces = deque()

        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == 0:
                    spaces.append((i,j))
        
        distance = 0
        while spaces:
            i, j = spaces.popleft()
            for r, c in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
                if r<0 or r==ROWS or c<0 or c==COLUMNS:
                    continue
                if grid[r][c] <= (grid[i][j] + 1):
                    continue
                grid[r][c] = grid[i][j] + 1
                spaces.append((r,c))

            