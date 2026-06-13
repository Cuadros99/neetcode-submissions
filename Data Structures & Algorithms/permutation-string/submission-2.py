class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = {}
        char_set = set()
        for c in s1:
            counter[c] = counter.get(c, 0) + 1
            char_set.add(c)
        l, r = 0, 0

        while r < len(s2):
            if s2[r] in counter:
                counter[s2[r]] -= 1

            if (r - l + 1) > len(s1):
                if s2[l] in char_set:
                    counter[s2[l]] += 1
                l += 1
            
            if not any(counter.values()):
                return True
            else:
                r+=1
        
        return False
        
        O(m*n*log(n))