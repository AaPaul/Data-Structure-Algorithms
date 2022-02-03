from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = 2 * len(s)
        ans = [""] * n
        
        n = len(spaces)
        i = 0
        ans_j = 0
        s_j = 0
        while i < n:
            if ans_j == spaces[i]:
                ans[ans_j] = " "
                i += 1
            else:
                ans[ans_j] = s[s_j]
                s_j += 1
            ans_j += 1
        return ''.join(ans)

s1 = Solution()
print(s1.addSpaces("LeetcodeHelpsMeLearn", [8,13,15]))