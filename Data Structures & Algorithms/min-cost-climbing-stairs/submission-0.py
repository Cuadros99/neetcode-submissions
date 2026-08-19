class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        
        path_cost = [0] * len(cost)
        path_cost[-1] = cost[-1]
        path_cost[-2] = cost[-2]

        for i in range(N-3, -1, -1):
            path_cost[i] = cost[i] + min(path_cost[i+1], path_cost[i+2])


        return min(path_cost[0], path_cost[1])











    
        #   [1, 2, 4] -> 2
        #   [1, 4, 2] -> 3