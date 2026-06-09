class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        past_num = set()
        n = len(nums)
        for i in range(n):
            if nums[i] in past_num:
                return True
            else:
                past_num.add(nums[i])
        return False