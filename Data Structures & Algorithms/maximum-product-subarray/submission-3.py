class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        global_max_prod = nums[0]
        max_prod = 1
        min_prod = 1

        for i in range(N):
            temp = max(nums[i], max_prod*nums[i], min_prod*nums[i])
            min_prod = min(nums[i], max_prod*nums[i], min_prod*nums[i])
            max_prod = temp
            global_max_prod = max(max_prod, global_max_prod)

        return global_max_prod






    # [2, 3, 4] -> 24
    # [-2, 3, 4] -> 12
    # [1, 2 , 3, -4] -> 6
    # [1, -2 , 3, -4] -> 24
    # [] -> 0

