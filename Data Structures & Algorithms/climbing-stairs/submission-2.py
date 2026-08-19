class Solution:
    def climbStairs(self, n: int) -> int:
        memory = {} 
        
        def dfs(num_steps):
            if num_steps < 0:
                return 0
            if num_steps == 0:
                return 1

            if num_steps not in memory:
                memory[num_steps] = dfs(num_steps-2) + dfs(num_steps-1)

            return memory[num_steps]

        return dfs(n)

    # O(2^n)


    #   n = 1 -> 1
    #   n = 2 -> 2 
    #   n = 3 -> 3