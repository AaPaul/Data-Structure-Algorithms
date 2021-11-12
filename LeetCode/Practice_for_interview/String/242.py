import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_cnt, t_cnt = map(collections.Counter, (s, t))
        if s_cnt.keys() == t_cnt.keys():
            return not sum((s_cnt - t_cnt).values())
        else:
            return False
if __name__ == "__main__":
    s1 = Solution()
    s = "anagram"
    t = "nagaram"
    print(s1.isAnagram(s, t))