class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = defaultdict(list)

        # 'a' - 'z'
        for s in strs:
            freq_counter = [0] * 26
            for l in s:
                asc_l = ord(l)
                if ord('A') <= asc_l <= ord('Z'):
                    asc_l -= (ord('A') - ord('a'))
                index = asc_l - ord('a')
                freq_counter[index] += 1

            freq_counter = tuple(freq_counter)

            anagrams_map[freq_counter].append(s)
        
        return list(anagrams_map.values())

