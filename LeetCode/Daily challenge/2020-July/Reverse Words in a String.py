class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(' ')
        l = list(filter(None, l))
        res = []
        l.reverse()
        for i in l:
            if i != ' ':
                res.append(i)
        str_res = " ".join(res)
        return str_res

    def reverseWords2(sefl, s: str) -> str:
        return " ".join(reversed(s.split()))

s1 = Solution()
# print(s1.reverseWords("the sky is blue"))
# print(list(s1.reverseWords("  hello world!  ")))
print(list(s1.reverseWords2("  hello world!  ")))


# filter() is faster than loop function for dropping None value
