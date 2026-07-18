class TrieNode:
    def __init__(self, val, is_end=False):
        self.val = val
        self.children = {}
        self.is_end = is_end

class PrefixTree:

    def __init__(self):
        self.root = TrieNode(None, False)

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter in curr.children:
                curr = curr.children[letter]
            else:
                curr.children[letter] = TrieNode(letter)
                curr = curr.children[letter]
        
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            if letter in curr.children:
                curr = curr.children[letter]
            else:
                return False

        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            if letter in curr.children:
                curr = curr.children[letter]
            else:
                return False

        return True
        



#   trie = PrefixTree()

#   trie.insert("card")
   
#   trie.search("card") -> True
#   trie.search("car") -> False
   
#   trie.starsWith("car") -> True

