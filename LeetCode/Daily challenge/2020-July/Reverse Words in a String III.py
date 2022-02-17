class Solution:
    def reverseWords(self, s: str) -> str:
        l = s[::-1].split()
        l.reverse()
        return " ".join(l)


s1 = Solution()
print(s1.reverseWords("Let's take LeetCode contest"))