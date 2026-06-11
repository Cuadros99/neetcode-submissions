class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = { n for n in nums}
        greater_len = 0

        for n in nums:
            if n-1 in num_set:
                continue
            i = n+1
            size = 1
            while i in num_set:
                size += 1
                i += 1
            if size > greater_len:
                greater_len = size

        return greater_len