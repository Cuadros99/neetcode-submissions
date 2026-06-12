class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ord_sum = sorted(nums)
        n = len(nums)
        res = set()
        for i in range(n):
            if i>0 and ord_sum[i-1] == ord_sum[i]:
                continue
            target = -ord_sum[i]

            l = i+1
            r = n-1

            while l < r:
                two_sum = ord_sum[l] + ord_sum[r]
                
                if two_sum > target:
                    r -= 1
                elif two_sum < target:
                    l += 1
                else:
                    res.add((ord_sum[i], ord_sum[l], ord_sum[r]))
                    r -=1
                

        return [list(t) for t in res]