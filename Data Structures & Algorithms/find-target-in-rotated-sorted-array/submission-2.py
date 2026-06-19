class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        min_value = [nums[0], 0]

        while l <= r:
            if nums[l] < nums[r]:
                if nums[l] < min_value[0]:
                    min_value[0] = nums[l]
                    min_value[1] = l

            m = (l+r)//2
            if nums[m] < min_value[0]:
                min_value[0] = nums[m]
                min_value[1] = m

            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1

        
        if target <= nums[n-1]:
            l = min_value[1]
            r = len(nums)
        elif target >= nums[0]:
            l = 0
            r = min_value[1]
        else:
            return -1

        while l <= r:
            m = (l+r)//2

            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m-1 
            else:
                return m

        return -1
        