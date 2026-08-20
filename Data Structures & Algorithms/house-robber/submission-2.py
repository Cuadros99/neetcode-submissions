class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for m in nums:
            temp = max(m + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2



    #   [1] -> 1
    #   [1, 2] -> 2
    #   [1, 2, 3] -> 4
    #   [1, 5, 3] -> 5
    #   [2, 5, 3, 1, 5] -> 10
