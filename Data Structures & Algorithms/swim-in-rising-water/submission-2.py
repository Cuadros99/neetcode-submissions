class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])

        visited_squares = set()
        heap_paths = [(grid[0][0], 0, 0)]

        max_height = grid[0][0]

        while (ROWS-1,COLUMNS-1) not in visited_squares:
            h, i, j = heapq.heappop(heap_paths)
            if (i,j) in visited_squares:
                continue
            visited_squares.add((i,j))
            max_height = max(h, grid[i][j])
            for ni, nj in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
                if ni < 0 or ni == ROWS or nj <0 or nj == COLUMNS:
                    continue
                if (ni,nj) in visited_squares:
                    continue
                heapq.heappush(heap_paths, (max_height,ni,nj))

        return max_height
        
