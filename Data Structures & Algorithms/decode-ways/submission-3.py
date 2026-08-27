class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [0] * len(s)
        dp[len(s)-1] = 1 if s[-1] != '0' else 0

        for i in range(len(s)-2, -1, -1):
            if s[i] == "0":
                continue
            res = dp[i+1]
            if i+1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] in "0123456")):
                res += dp[i+2] if i+2 < len(s) else 1
            dp[i] = res

        return dp[0]

            

        
        #   12 -> 2
        #   10 -> 1
        #   26 -> 2
        #   264571 - 
