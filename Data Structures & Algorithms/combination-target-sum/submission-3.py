class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i: int, sol: List[int], somm: int):
            if i >= len(nums):
                return
            elif somm > target:
                return
            elif somm == target:
                res.append(sol.copy())
                return
            
            sol.append(nums[i])
            backtrack(i, sol, somm + nums[i])
            sol.pop()

            backtrack(i+1, sol, somm)

        backtrack(0, [], 0)

        return res

