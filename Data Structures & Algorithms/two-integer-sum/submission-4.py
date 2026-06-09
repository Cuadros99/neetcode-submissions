class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i, n in enumerate(nums):
            hashmap[n] = i

        for j, n in enumerate(nums):
            other_n = target - n
            i_other_n = hashmap.get(other_n, None)
            if i_other_n and i_other_n != j:
                return [j, i_other_n]



                