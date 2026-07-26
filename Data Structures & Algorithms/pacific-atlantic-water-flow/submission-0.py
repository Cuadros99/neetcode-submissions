class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLUMNS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        for i in range(ROWS):
            for j in range(COLUMNS):
                if j == 0 or i == 0:
                    pacific.add((i,j))
                if i == (ROWS-1) or j == (COLUMNS-1):
                    atlantic.add((i,j))

        def dfs(i,j, ocean, visited):
            for r,c in [(i+1,j), (i-1,j), (i,j-1), (i,j+1)]:
                if r not in range(ROWS) or c not in range(COLUMNS):
                    continue
                if heights[r][c] < heights[i][j]:
                    continue
                if (r,c) in visited:
                    continue
                visited.add((r,c))
                if ocean:
                    pacific.add((r,c))
                else:
                    atlantic.add((r,c))
                dfs(r,c, ocean, visited)
                


        for i,j in list(pacific):
            dfs(i,j, True, set())

        for i,j in list(atlantic):
            dfs(i,j, False, set())
        
        output = [cell for cell in pacific if cell in atlantic]

        return output




    #    [ 1  2]
    #    [ 2  1]

    #    [ 1  2  3]
    #    [ 2  1  3]
    #    [ 2  2  3] 
