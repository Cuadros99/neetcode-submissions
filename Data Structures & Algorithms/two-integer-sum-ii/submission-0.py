class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while r > l:

            nums_sum = numbers[l] + numbers[r]
            
            if nums_sum > target:
                r -= 1

            if nums_sum < target:
                l += 1

            if nums_sum == target:
                return [l + 1, r + 1]







        
        