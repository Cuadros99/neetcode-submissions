class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while j>=i:
            if not s[i].isalnum() or not s[i].isascii():
                i += 1
                continue

            if not s[j].isalnum() or not s[j].isascii():
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                return False
            
            i+=1
            j-=1
        
        return True