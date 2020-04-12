class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
            def build(S):
                ans = []
                for c in S:
                    if c != '#':
                        ans.append(c)
                    elif ans:
                        ans.pop()
                return "".join(ans)

            return build(S) == build(T)
        # # if (len(S) == len(T)):
        # #     for i in range(len(S)):
        # #         if
        #
        # S = S.replace(" ", "")
        # T = T.replace(" ", "")
        # if len(S) == len(T):
        #     if S[0] == T[0] or S[-1] == T[-1]:
        #         return True
        #     else:
        #         return False
        # else:
        #     return False


s1 = Solution()

print(s1.backspaceCompare("xywrrmp", "xywrrm#p"))

# Note: Why this question is asking for the application of the stack?