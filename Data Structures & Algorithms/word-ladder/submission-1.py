class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = {beginWord}
        output = 0
        wordIndex = [1] * len(wordList)

        def backtracking(word):
            nonlocal output
            result = False
            if word == endWord:
                output = min(len(visited), output) if output > 0 else len(visited)
                return True
            for i, new_word in enumerate(wordList):
                if new_word in visited or wordIndex[i] == 0:
                    continue
                if self.isJustOneChange(new_word, word):
                    visited.add(new_word)
                    if backtracking(new_word):
                        result = True
                    else:
                        wordIndex[i] = 0
                    visited.remove(new_word)
                        
            return result
        
        backtracking(beginWord)

        return output
                



    def isJustOneChange(self, word_a, word_b):
        count = 0
        for i in range(len(word_a)):
            if word_a[i] != word_b[i]:
                count += 1
                if count == 2: 
                    return False
        return True