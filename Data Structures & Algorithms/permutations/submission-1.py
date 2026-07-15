class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(selected, sol):
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for n in nums:
                if n in selected:
                    continue
                sol.append(n)
                selected.add(n)
                backtrack(selected, sol)
                sol.pop()
                selected.remove(n)

        backtrack(set(), [])

        return res
        