class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.queen_spaces = []
        res = []

        def backtrack(i, j, k, board):
            if k == 0:
                solution = ["".join(r) for r in board ]
                res.append(solution)
                return
            if i == n-1 and j >= n:
                return
            if j >= n:
                backtrack(i+1, 0, k, board)
                return    
            if self.is_allowed(i, j):
                board[i][j] = "Q"
                self.queen_spaces.append((i,j))
                backtrack(i, j+1, k-1, board)
                self.queen_spaces.pop()
                board[i][j] = "."
                backtrack(i, j+1, k, board)
            else:
                backtrack(i, j+1, k, board)
        
        board = [["."]*n for _ in range(n)]
        backtrack(0, 0, n, board)
        return res

    def is_allowed(self, i, j):
        for queen in self.queen_spaces:
            r, c = queen
            if r == i or c == j or abs(r-i) == abs(c-j):
                return False
        return True
                


