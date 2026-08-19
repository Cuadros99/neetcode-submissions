class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        
        first = cost[-2]
        second = cost[-1]

        for i in range(N-3, -1, -1):
            print(first)
            print(second)
            temp = first
            first = cost[i] + min(first, second)
            second = temp
            


        return min(first, second)











    
        #   [1, 2, 4] -> 2
        #   [1, 4, 2] -> 3