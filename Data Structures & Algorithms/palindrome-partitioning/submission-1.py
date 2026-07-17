def is_palindrome(substr: str):
    l, r = 0, len(substr)-1
    while l <= r:
        if substr[l] != substr[r]:
            return False
        l += 1
        r -= 1

    return True

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(i, sol):
            if i >= len(s):
                res.append(sol[:])
                return
            
            substr = ""
            while i < len(s):
                substr += s[i]
                if is_palindrome(substr):
                    sol.append(substr)
                    backtrack(i+1, sol)
                    sol.pop()
                i += 1

        backtrack(0, [])

        return res
                
        
    
    
    
    #    "a" -> [["a"]]
    #    "abc" -> [["a", "b", "c"]]
    #    "aabc" -> [["a", "a", "b", "c"], ["aa", "b", "c"]]