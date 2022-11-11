
from typing import List
'''
We define dp[i] to indicate whether the string consisting of the first i
characters of the string s can be split by spaces into several words that appear in the dictionary

https://leetcode.com/problems/word-break/discuss/2510121/Python3-interview-style-implementations-(top-downbottom-up-DP-Trie)-with-explanations


https://leetcode.cn/problems/word-break/solution/java-1ms-xun-xu-jian-jin-cong-cuo-wu-cha-umpv/
'''

class TreeNode:
    def __init__(self):
        self.mp = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TreeNode()
        self.failed = [False] * 301
        
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.mp:
                node.mp[ch] = TreeNode()
            node = node.mp[ch]
        node.isEnd = True
    # @lru_cache
    def search(self, s, i):
        if self.failed[i]:
            return False
        if i >= len(s):
            return True
        node = self.root
        while i < len(s):
            if s[i] not in node.mp:
                return False
            node = node.mp[s[i]]
            if node.isEnd:
                if self.search(s, i+1):
                    return True
                self.failed[i+1] = True
            i += 1
        return False
            
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        return trie.search(s, 0)
        
s = "catsandogcat"
w = ["cats","dog","sand","and","cat","an"]
s1 = Solution()
print(s1.wordBreak(s, w))