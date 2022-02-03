from typing import List


class Solution:
    def helper(self, l, i):
        if i in l:
            return True
        else:
            return False
        
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        
        dp = [0] * (n + 1)
        skip = [0] * (n + 1)
        dp[0] = questions[0][0]
        skip[0] = questions[0][1] + 1
        for i in range(1, n):
            if i not in skip:
                dp[i] = questions[i][0]
                skip[i] = questions[i][1] + i + 1
            else:
                t = skip.copy()
                _max = -1
                # i_max = -1
                cnt = 0
                while self.helper(t, i):
                    idx = t.index(i)
                    t.pop(idx)
                    idx += cnt
                    _max = max(questions[idx][0], _max)
                    cnt += 1
                    # val = t.pop(idx)
                    # if val > _max:
                    #     _max = val
                    #     i_max = idx
                    
                dp[i] = _max + questions[i][0]
                skip[i] = questions[i][1] + i + 1
        return max(dp)
                

s1 = Solution()
# q = [[3,2],[4,3],[4,4],[2,5]]
# q = [[1,1],[2,2],[3,3],[4,4],[5,5]]
q = [[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]]
print(s1.mostPoints(q))