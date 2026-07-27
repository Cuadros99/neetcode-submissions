class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLUMNS = len(board), len(board[0])
        not_surrounded = set()
        
        def dfs(i,j):
            if i not in range(ROWS) or j not in range(COLUMNS):
                return
            if (i,j) in not_surrounded or board[i][j] == "X":
                return
            not_surrounded.add((i,j))
            
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        for i in range(ROWS):
            for j in range(COLUMNS):
                if i in [0,ROWS-1] or j in [0, COLUMNS-1]:
                    dfs(i,j)
            
        for i in range(ROWS):
            for j in range(COLUMNS):
                if board[i][j] == 'O' and (i,j) not in not_surrounded:
                    board[i][j] = "X"



