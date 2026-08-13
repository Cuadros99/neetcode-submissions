class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adjacency_map = {l: set() for w in words for l in w}

        for i in range(len(words)-1):
            word_a, word_b = words[i], words[i+1]
            min_len = min(len(word_a), len(word_b))
            
            if (len(word_a) > len(word_b)
                and word_a[:min_len] == word_b[:min_len]):
                return ""

            for j in range(min_len):
                if word_a[j] != word_b[j]:
                    adjacency_map[word_a[j]].add(word_b[j])
                    break

        visited = {}
        alphabet = []

        def dfs(l):
            if l in visited:
                return visited[l]

            visited[l] = True

            for neighbor in adjacency_map[l]:
                if dfs(neighbor):
                    return True

            alphabet.append(l)
            visited[l] = False
            return visited[l]

        for l in adjacency_map:
            if dfs(l):
                return ""


        alphabet.reverse()

        return "".join(alphabet)



    #"za", "zb", "ka", "kc"
    
    #"za", "zb", "kc", "kb"

    #"d", "e", "f", "a" -> "defa"
    #"dcs", "dca", "dck" -> "sakdc"
    #"cba", "bac", "abc" -> "cba"
