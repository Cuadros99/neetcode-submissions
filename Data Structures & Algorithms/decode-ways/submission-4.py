class Solution:
    def numDecodings(self, s: str) -> int:
        
        first, second = 1 if s[-1] != "0" else 0, 0
        
        for i in range(len(s)-2, -1, -1):
            if s[i] == "0":
                res = 0
            else:
                res = first
                if i+1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] in "0123456")):
                    res += second if i+2 < len(s) else 1
            temp = first
            first = res
            second = temp

        return first

            

        
        #   12 -> 2
        #   10 -> 1
        #   26 -> 2
        #   264571 - 
