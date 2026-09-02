class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(total):

            if total == 0:
                return 0

            if total not in memo:
                res = float('inf')
                for coin in coins[::-1]:
                    if coin <= total:
                        res = min(dfs(total-coin), res)
                memo[total] = res + 1

            return memo[total]

        res = dfs(amount)
        return res if res <= amount else -1

        
            
            













        #   [1, 3, 10], target= 25 -> 5
        #   [1, 5, 8], target= 3 -> 3