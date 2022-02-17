from typing import List

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        s_list = list(s)
        for i in shift:
            for j in range(i[1]):
                if i[0] == 0:
                    temp = s_list.pop(0)
                    s_list.append(temp)
                else:
                    temp = s_list.pop(-1)
                    s_list.insert(0, temp)

        s_new = ''.join(map(str, s_list))  # List to str
        return s_new

        # print(s_new)

s1 = Solution()
# s1.stringShift("abc", [[0,1],[1,2]])
s1.stringShift("abcdefg", [[1,1],[1,1],[0,2],[1,3]])