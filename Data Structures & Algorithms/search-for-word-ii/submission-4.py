class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.createTrie(words)
        res = set()

        def backtrack(i, j, node, visited: set):
            if node.word:
                res.add(node.word)
            if i < 0 or i == len(board) or j < 0 or j == len(board[0]):
                return
            if (i, j) in visited:
                return    
            if board[i][j] not in node.children:
                return

            visited.add((i,j))
            backtrack(i+1, j, node.children[board[i][j]], visited)
            backtrack(i, j+1, node.children[board[i][j]], visited)
            backtrack(i-1, j, node.children[board[i][j]], visited)
            backtrack(i, j-1, node.children[board[i][j]], visited)
            visited.remove((i,j))
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in self.root.children:
                    backtrack(i, j, self.root, set())

        return list(res)

    def createTrie(self, words):
        self.root = TrieNode()
        
        for word in words:
            curr = self.root
            for letter in word:
                if letter not in curr.children:
                    curr.children[letter] = TrieNode()
                curr = curr.children[letter]
            curr.word = word


        





#[[b a c k]
# [t t c a]
# [a c d r]]    [bat cat car back catch] -> [bat cat car back]
#               [bath, kiss, window] -> []
#
#[[c a]
# [t r]]         [car, cat, rat] -> [car]