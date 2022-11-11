'''
Introduction of Trie: https://segmentfault.com/a/1190000040801084

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.


'''


class TreeNode:
    def __init__(self):
        self.isEnd = False
        self.mp = {}

class Trie:

    def __init__(self):
        self.root = TreeNode()


    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.mp:
                node.mp[ch] = TreeNode()
            node = node.mp[ch]
        node.isEnd = True



    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.mp:
                return False
            node = node.mp[ch]
        return node.isEnd == True

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.mp:
                return False
            node = node.mp[ch]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)