class Solution:
    def rob(self, nums: List[int]) -> int:
        memory = {}

        def dfs(i):
            if i >= len(nums):
                return 0
            if i not in memory:
                memory[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return memory[i]

        return dfs(0)



    #   [1] -> 1
    #   [1, 2] -> 2
    #   [1, 2, 3] -> 4
    #   [1, 5, 3] -> 5
    #   [2, 5, 3, 1, 5] -> 10
