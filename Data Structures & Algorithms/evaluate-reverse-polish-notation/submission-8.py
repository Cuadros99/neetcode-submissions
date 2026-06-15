class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        operators = {
            '+': self._sum, 
            '-': self._minus,
            '*': self._times, 
            '/': self._divide
            }
        res = 0

        for t in tokens:
            if t in operators:
                r = stack.pop()
                l = stack.pop()
                res = operators[t](l, r)
                stack.append(res)
            else:
                stack.append(int(t))

        return res

    def _sum(self, l, r):
        return l+r

    def _minus(self, l, r):
        return l-r

    def _times(self, l, r):
        return l*r

    def _divide(self, l, r):
        return int(l/r)
