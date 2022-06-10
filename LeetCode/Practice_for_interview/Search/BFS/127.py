from collections import deque
class Solution:
    def match(self, target, s):
        cnt = 0
        for t, ch in zip(target, s):
            if t == ch:
                cnt += 1

        return cnt == len(s) - 1

    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        q = deque([beginWord])
        visited = {}
        for w in wordList:
            visited[w] = 0
        level = 0
        while q:
            size = len(q)
            level += 1
            for _ in range(size):
                curr = q.popleft()
                if self.match(curr, endWord):
                    return level+1
                for word in wordList:
                    if visited[word]:
                        continue

                    ret = self.match(curr, word)
                    if ret:
                        visited[word] = 1
                        q.append(word)
                    
                        
        
        return 0