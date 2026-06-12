class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        seen = set()
        max_len = 0


        while r < len(s):
            if s[r] in seen:
                seen.remove(s[l])
                l+=1
            else:
                seen.add(s[r])
                r+=1
            
            max_len = max(max_len, r-l)

        return max_len