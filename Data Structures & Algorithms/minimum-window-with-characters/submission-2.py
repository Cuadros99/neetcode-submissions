class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = {}
        res = (len(s) + 1, "")
        for c in t:
            counter[c] = 1 + counter.get(c, 0)

        l, r = 0, 0
        need = len(counter)
        while r < len(s):
            if s[r] in counter:
                counter[s[r]] -= 1
                if counter[s[r]] == 0:
                    need -= 1
            
            while need == 0:
                if res[0] > (r - l + 1):
                    res = (r - l + 1, s[l:r+1])
                
                if s[l] in counter:
                    counter[s[l]] += 1
                    if counter[s[l]] == 1:
                        need += 1
                l += 1

            r += 1

        return res[1]