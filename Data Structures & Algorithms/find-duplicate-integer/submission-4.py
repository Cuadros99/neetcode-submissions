class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = abs(nums[i])
            if nums[n-1] < 0:
                return n
            else:
                nums[n-1] = nums[n-1] * -1
