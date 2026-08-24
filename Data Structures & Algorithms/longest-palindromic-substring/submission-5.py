class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.word = s
        self.memoization = {}
        max_palin = (0,0,0)
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if self.is_palindrome(i, j):
                    max_palin = (j-i+1, i, j) if j-i+1 > max_palin[0] else max_palin

        return s[max_palin[1]:max_palin[2]+1]
    
    def is_palindrome(self, i, j):
        if (i,j) not in self.memoization: 
            if self.word[i] == self.word[j]:
                self.memoization[(i,j)] = True if j - i <= 2 else self.is_palindrome(i+1, j-1)
            else:
                self.memoization[(i,j)] = False

        return self.memoization[(i,j)]
            
                



      #  "a" -> "a"
      #  "aba" -> "aba"
      #  "banana" -> "anana"
      #  "barata" -> "ara" or "ata"
         