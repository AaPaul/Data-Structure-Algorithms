from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        res = []
        m = len(s)
        for i in range(m):
            cur = startPos.copy()
            cnt = 0
            for j in range(i, m):
                if s[j] == "L":
                    cur[1] -= 1
                elif s[j] == "R":
                    cur[1] += 1
                elif s[j] == "U":
                    cur[0] -= 1
                else:
                    cur[0] += 1
                if cur[0] < 0 or cur[0] >= n or cur[1] >= n or cur[1] < 0:
                    break
                cnt += 1
            res.append(cnt)
        return res

s1 = Solution()
n = 3
startPos = [0, 1]
s = "RRDDLU"
print(s1.executeInstructions(n, startPos, s))