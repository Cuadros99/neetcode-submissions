class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, sol, sommation):
            if sommation == target:
                res.append(sol[:])
                return
            if i >= len(candidates):
                return
            if sommation > target:
                return
            
            sol.append(candidates[i])
            backtrack(i+1, sol, sommation + candidates[i])
            sol.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1, sol, sommation)

        backtrack(0, [], 0)

        return res

       
       
       
       
       
       # [1] t=2 -> []
       # [1, 2, 3] t=3 -> [[1,2], [3]]
       # [1, 1, 2, 4, 6] t=6 -> [[1,1,4], [2,4], [6]]
       # [1, 1, 2, 4, 6] t=5 -> [[1,4]]
