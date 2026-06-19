class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        res = max_pile

        l, r = 1, max_pile
        while l <= r:
            t = 0
            k = (l+r)//2
            for p in piles:
                t += math.ceil(p/k)

            if t <= h:
                res = k
                r = k - 1
            elif t > h:
                l = k + 1
            else:
                return k

        return res



