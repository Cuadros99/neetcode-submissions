class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def subsequence(i, last):
            if (i,last) not in memo:
                res = []
                if i >= len(nums):
                    return 0
                if last == -1 or nums[i] > nums[last]:
                    res.append(1 + subsequence(i+1, i))
                
                res.append(subsequence(i+1, last))
                memo[(i,last)] = max(res)
                
            return memo[(i,last)]

        return subsequence(0, -1)




    #   [1, 2, 3, 4] -> 4
    #   [2, 1, 3, 4] -> 3
    #   [4, 1, 3, 2] -> 2
    #   [4, 3, 2, 1] -> 1