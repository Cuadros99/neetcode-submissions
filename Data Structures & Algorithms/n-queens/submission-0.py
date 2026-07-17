class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.allowed_spaces = [[0]*n for _ in range(n)]
        self.allowed_count = n*n
        res = []

        def backtrack(i, j, k, board):
            if k == 0:
                solution = ["".join(r) for r in board ]
                res.append(solution)
                return
            if self.allowed_count < k:
                return
            if i == n-1 and j >= n:
                return
            if j >= n:
                backtrack(i+1, 0, k, board)
                return    
            if self.allowed_spaces[i][j] == 0:
                board[i][j] = "Q"
                self.update_allowed_spaces(i, j, True)
                backtrack(i, j+1, k-1, board)
                self.update_allowed_spaces(i, j, False)
                board[i][j] = "."
                backtrack(i, j+1, k, board)
            else:
                backtrack(i, j+1, k, board)
        
        board = [["."]*n for _ in range(n)]
        backtrack(0, 0, n, board)
        return res

    def update_allowed_spaces(self, i, j, adding: bool):
        n = self.n
        for r in range(n):
            for c in range(n):
                if r == i or c == j or abs(r-i) == abs(c-j):
                    if adding and self.allowed_spaces[r][c] == 0:
                        self.allowed_count -= 1
                    self.allowed_spaces[r][c] += 1 if adding else -1

                    if not adding and self.allowed_spaces[r][c] == 0:
                        self.allowed_count += 1
                    


