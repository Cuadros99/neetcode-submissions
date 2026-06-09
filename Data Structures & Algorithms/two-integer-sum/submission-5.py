class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()

        for j, n in enumerate(nums):
            diff = target - n
            
            if diff in hashmap:
                return [hashmap[diff], j]

            hashmap[n] = j



                