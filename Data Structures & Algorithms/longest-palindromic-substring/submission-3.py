class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palin = (0,0,0)

        for i in range(len(s)):

            l, r = i, i
            curr = None

            while l >=0 and r < len(s):
                if s[l] == s[r]:
                    max_palin = (r-l+1, l, r) if r-l+1 > max_palin[0] else max_palin
                    l -= 1
                    r += 1
                else:
                    break
                
            
            l, r = i, i+1
            while l >=0 and r < len(s):
                if s[l] == s[r]:
                    max_palin = (r-l+1, l, r) if r-l+1 > max_palin[0] else max_palin
                    l -= 1
                    r += 1
                else:
                    break
                

        return s[max_palin[1]:max_palin[2]+1]

                



      #  "a" -> "a"
      #  "aba" -> "aba"
      #  "banana" -> "anana"
      #  "barata" -> "ara" or "ata"
         