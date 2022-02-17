class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            # print(ord(s[i])-ord('A')+1)
            res += (ord(s[i]) - ord('A') + 1) * 26 ** (len(s) - i - 1)

        return res


# NOTE: we need to use `ord()` function to implement the subtraction of letters in python.