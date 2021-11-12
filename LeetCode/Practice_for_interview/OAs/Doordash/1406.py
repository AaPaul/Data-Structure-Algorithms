from typing import List


# class Solution:
#         def stoneGameIII(self, stoneValue: List[int]) -> str:
#             n = len(stoneValue)

#             suffix_sum = [0] * (n - 1) + [stoneValue[-1]]
#             for i in range(n - 2, -1, -1):
#                 suffix_sum[i] = suffix_sum[i + 1] + stoneValue[i]

#             # The value should be 0 if there is No stone
#             f = [0] * n + [0]

#             for i in range(n - 1, -1, -1):
#                 f[i] = suffix_sum[i] - min(f[i+1: i+4])

#             total = sum(stoneValue)

#             if f[0] * 2 == total:
#                 return "Tie"
#             else:
#                 return "Alice" if f[0] * 2 > total else "Bob"
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        # 边界情况，当没有石子时，分数为 0
        f = [-10**9] * n + [0]
        for i in range(n - 1, -1, -1):
            pre = 0
            for j in range(i + 1, min(i + 3, n) + 1):
                pre += stoneValue[j - 1]
                f[i] = max(f[i], pre - f[j])
        
        if f[0] == 0:
            return "Tie"
        else:
            return "Alice" if f[0] > 0 else "Bob"

if __name__ == "__main__":
    S1 = Solution()
    case1 = [1, 2, 3, 6]
    print(S1.stoneGameIII(case1))