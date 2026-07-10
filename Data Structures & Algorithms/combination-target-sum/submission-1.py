class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, sol, summation):
            if summation == target:
                res.append(sol[:])
                return
            if i >= len(nums) or summation > target:
                return 
            
            sol.append(nums[i])
            backtrack(i, sol, summation + nums[i])
            sol.pop()
          
            backtrack(i+1, sol, summation)

        backtrack(0, [] , 0)

        return res
    
    
    
    
    
    
#    [1, 2, 3] target =1 -> [[1]]
#    [1, 2, 3] target =3 -> [[1,1,1],[1,2], [3]]
#    [] -> []
#    [2] target = 3 -> []

    