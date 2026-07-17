class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        res = []

        def backtrack(i, sol):
            if i >= len(digits):
                if sol:
                    res.append("".join(sol))
                return

            for letter in nums_map[digits[i]]:
                sol.append(letter)
                backtrack(i+1, sol)
                sol.pop()
        
        backtrack(0, [])

        return res