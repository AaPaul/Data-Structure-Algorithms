class Solution:
    def solution(self, s1:str, s2:str) -> bool:
        s_new = s1+s1
        return True if s2 in s_new else False

    # 模拟取余
    def solution2(self, s1:str, s2:str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        i = 0
        while i != n1:
            if s1[i] == s2[0]:
                j = 1
                while j < n2 and s1[(i+j) % n1] == s2[j]:
                    j += 1
                if j == n2:
                    return True
            i += 1
        return False



if __name__ == "__main__":
    """
    给定两个字符串s1和s2, 要求判定s2是否能够被通过s 作循环移位 ( rotate )得到的字符串包含。
    例如, 给定s1 = AABCD和s2 = CDAA,返回 true;给定s1 = ABCD和s2 = ACBD, 返回 false。
    """
    s = Solution()
    s1 = "AABCD"
    s2 = "CDAA"
    # s1="ABCD"
    # s2="ACBD"
    print(s.solution2(s1, s2))