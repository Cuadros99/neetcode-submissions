class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        
        fresh_counter = 0
        queue = deque()
        time_last_rotten = 0

        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == 1:
                    fresh_counter += 1
                if grid[i][j] == 2:
                    queue.append((i,j,0))

        while queue:
            i, j, t = queue.popleft()

            for r, c in [(i+1, j), (i-1, j), (i, j+1), (i,j-1)]:
                if r<0 or r==ROWS or c<0 or c==COLUMNS:
                    continue
                if grid[r][c] == 1:
                    queue.append((r,c,t+1))
                    grid[r][c] = 2
                    fresh_counter -= 1
                    time_last_rotten = max(time_last_rotten, t+1)
        
        return time_last_rotten if fresh_counter == 0 else -1
        











   #     [[1 1]      [[1 2]          2 min
   #      [1 2]]      [2 2]]

   #     [[1 0]      -1
   #      [0 2]]      

