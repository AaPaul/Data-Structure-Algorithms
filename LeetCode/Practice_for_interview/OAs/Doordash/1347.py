import collections

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_cnt, t_cnt = map(collections.Counter, (s, t))
        
        return sum((s_cnt - t_cnt).values())