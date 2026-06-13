class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = set(s)
        max_len = 0

        for c in char_set:
            counter = 0
            l, r = 0,0
            
            while r < len(s):
                if s[r] == c:
                    counter += 1
                while (r - l + 1) - counter > k:
                    if s[l] == c:
                        counter -= 1
                    l += 1
                
                max_len = max(max_len, r - l + 1)

                r += 1
        
        return max_len

   



        
