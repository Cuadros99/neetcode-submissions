class TrieNode:
    def __init__(self, val, is_end=False):
        self.val = val
        self.children = {}
        self.is_end = is_end

class WordDictionary:

    def __init__(self):
        self.root = TrieNode(None)

    def addWord(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode(letter)
            curr = curr.children[letter]
        curr.is_end = True

    def search(self, word: str) -> bool:
        res = False

        def backtrack(root: TrieNode, i):
            nonlocal res
            if res:
                return
            if i > len(word):
                return
            if i == len(word):
                res = root.is_end
                return

            if word[i] in root.children:
                backtrack(root.children[word[i]], i+1)
                return
            if word[i] == ".":
                for node in root.children.values():
                    backtrack(node, i+1)
        
        backtrack(self.root, 0)

        return res


#   word_dict = WordDictionary()
#   word_dict.addWord("card")
#   word_dict.search("card") -> True
#   word_dict.search("car") -> False
#   word_dict.search("car.") -> True
#   word_dict.search("card.") -> False
#   word_dict.search("c.rd") -> True