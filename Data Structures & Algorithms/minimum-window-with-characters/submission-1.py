class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = {}
        res = (len(s) + 1, "")
        for c in t:
            counter[c] = 1 + counter.get(c, 0)

        l, r = 0, 0

        while r < len(s):
            if s[r] in counter:
                counter[s[r]] -= 1
            
            while all(v<=0 for v in counter.values()):
                if res[0] > (r - l + 1):
                    res = (r - l + 1, s[l:r+1])
                
                if s[l] in counter:
                    counter[s[l]] += 1
                l += 1

            r += 1

        return res[1]