class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        res = False

        def backtrack(i: int, j: int, counter: List[str], visited: set):
            nonlocal res
            if res:
                return
            if counter == len(word):
                res = True
                return
            if 0 > i or i >= len(board) or 0 > j or j >= len(board[0]):
                return
            if board[i][j] != word[counter] or (i,j) in visited:
                return
            
            counter += 1
            visited.add((i, j))
            backtrack(i, j+1, counter, visited)
            backtrack(i+1, j, counter, visited)
            backtrack(i, j-1, counter, visited)
            backtrack(i-1, j, counter, visited)
            counter -= 1
            visited.remove((i, j))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    backtrack(i, j, 0, set())
                    if res:
                        return True
        
        return res

  #  [[A, T, C]
  #   [H, D, B]] word = "hat" -> true
  #  [[A, T, C]
  #   [H, B, B]] word = "bat" -> false