class Solution:
    def countSubstrings(self, s: str) -> int:
        self.memo = {}
        pal_count = 0 

        for l in range(len(s)-1, -1, -1):
            for r in range(l, len(s)):
                if s[l] == s[r] and (r-l<=2 or self.memo[(l+1,r-1)]):
                    self.memo[(l,r)] = True
                    pal_count += 1
                else:
                    self.memo[(l,r)] = False

        return pal_count






        # a -> 1
        # ba -> 2
        # aa -> 3
        # aba -> 4
