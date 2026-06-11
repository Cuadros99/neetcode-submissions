class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_check = [set() for _ in range(9)]
        columns_check = [set() for _ in range(9)] 
        squares_check = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                e = board[i][j]
                if e != '.':
                    if e in rows_check[i] or e in columns_check[j]:
                        return False
                    rows_check[i].add(e)
                    columns_check[j].add(e)

                    r_index = i // 3
                    c_index = j // 3
                    if e in squares_check[r_index][c_index]:
                        return False
                    squares_check[r_index][c_index].add(e)

        return True
        