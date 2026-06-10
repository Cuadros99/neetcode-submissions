class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        preffix_prod = [1] * n
        suffix_prod = [1] * n 
        res = [1] * n 

        for i in range(1, n):
            preffix_prod[i] = preffix_prod[i-1] * nums[i-1]
        
        for j in range(n-2, -1, -1):
            suffix_prod[j] = suffix_prod[j+1] * nums[j+1]

        for k in range(n):
            res[k] = preffix_prod[k] * suffix_prod[k]

        return res
         