# 524. Longest Word in Dictionary through Deleting (Medium)
# Sub string: 
# 1). len(substr) < len(str)
# 2). elements in substr have corresponding elements in parent string

from typing import List

class Solution:
    def ifSubstr(self, s:str, target:str) -> bool:
        if len(s) < len(target):
            return False
        idx_t = 0
        idx_s = 0
        while idx_s < len(s):
            if s[idx_s] == target[idx_t]:
                idx_t += 1
            if idx_t == len(target):
                return True
            idx_s += 1
        return False

    def minLexicographicalOrder(self, s1:str, s2:str) -> str:
        for i, j in zip(s1, s2):
            if ord(i) > ord(j):
                return s2
            elif ord(i) < ord(j):
                return s1
            else:
                continue
        return s1
        
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        _max = -1
        res = ""
        for l in dictionary:
            if self.ifSubstr(s, l):
                if _max < len(l):
                    _max = len(l)
                    res = l
                elif _max == len(l):
                    res = self.minLexicographicalOrder(res, l)
                else:
                    continue
        return res