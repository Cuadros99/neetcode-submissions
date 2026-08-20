class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        rob1, rob2 = 0, 0
        if len(nums) == 1:
            return nums[0]

        for n in nums[0:N-1]:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        first_house = rob2
        rob1, rob2 = 0, 0

        for n in nums[1:N]:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return max(first_house, rob2)




    #  [] -> 0
    #  [1, 2, 3] -> 3
    #  [1, 2, 3, 4] -> 6