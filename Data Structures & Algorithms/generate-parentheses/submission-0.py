class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(i, sol, num_open, num_close):
            if i > 2*n:
                res.append("".join(sol))
                return

            if num_open < n:
                sol.append('(')
                backtrack(i+1, sol, num_open+1, num_close)
                sol.pop()

            if num_open > num_close:
                sol.append(')')
                backtrack(i+1, sol, num_open, num_close+1)
                sol.pop()

            
        backtrack(1, [], 0, 0)

        return res
    
    
    
    
    #   n = 1 -> ["()"]
    #   n = 2 -> ["()()", "(())"]
    #   n = 3 -> ["()()()", "(())()", "()(())", "(()())", "((()))"]