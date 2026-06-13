class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_1 = {}
        for c in s1:
            counter_1[c] = counter_1.get(c, 0) + 1

        counter_2 = counter_1.copy()
        l, r = 0, 0

        while r < len(s2):
            if s2[r] in counter_2:
                counter_2[s2[r]] -= 1

            if (r - l + 1) > len(s1):
                if s2[l] in counter_1:
                    counter_2[s2[l]] += 1
                l += 1
            
            if not any(counter_2.values()):
                return True
            else:
                r+=1
        
        return False
            

        
        