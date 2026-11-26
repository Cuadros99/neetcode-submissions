class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        nums_set = { n for n in nums}

        for n in nums_set:
            if n-1 not in nums_set:
                counter = 1
                i = n + 1
                while i in nums_set:
                    i+=1
                    counter += 1
                max_len = max(max_len, counter)

        return max_len
    
    
    
    
    
    
    # [1, 3, 2, 5] -> 3   [1, 2, 3]

    