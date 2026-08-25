class Solution:
    def countSubstrings(self, s: str) -> int:
        palin_counter = 0

        for i in range(len(s)):
            
            # odd palindromes
            l, r = i, i 
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    palin_counter += 1
                    l -= 1
                    r += 1
                else:
                    break

            # even palindromes
            l, r = i, i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    palin_counter += 1
                    l -= 1
                    r += 1
                else:
                    break
        
        return palin_counter




        # a -> 1
        # ba -> 2
        # aa -> 3
        # aba -> 4
