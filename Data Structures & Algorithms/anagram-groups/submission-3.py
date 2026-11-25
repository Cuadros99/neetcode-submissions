class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hash_map = defaultdict(list)

        for s in strs:
            ch_freq = [0]*26
            
            for c in s:
                ch_freq[ord(c) - ord('a')] += 1
            
            hash_map[tuple(ch_freq)].append(s)

        for group in hash_map.values():
            res.append(group)

        return res




    # O(n*m*log(m)) 







    #   ['act', 'cat', 'abc', 'def', 'fed'] -> [ ['act', 'cat'], ['abc'], ['def', 'fed'] ]