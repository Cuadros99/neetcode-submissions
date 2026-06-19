class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0]:
            return nums[0]
        
        l, r = 0, len(nums) - 1

        while (r - l) > 1:
            m = (l+r)//2

            if nums[l] < nums[m]:
                l = m
            else:
                r = m

        return nums[r]


       

  