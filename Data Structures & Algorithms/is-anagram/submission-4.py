class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hashmap = dict()
        t_hashmap = dict()

        for i in s:
            if i in s_hashmap:
                s_hashmap[i] += 1
            else:
                s_hashmap[i] = 1
        
        for j in t:
            if j in t_hashmap:
                t_hashmap[j] += 1
            else:
                t_hashmap[j] = 1

        for i in s_hashmap:
            if i not in t_hashmap:
                return False
            else:
                i_counter_s = s_hashmap[i]
                i_counter_t = t_hashmap[i]
                if i_counter_s != i_counter_t:
                    return False
        return True
