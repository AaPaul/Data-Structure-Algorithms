"""
s = "I am a student"
Return "student a am I"
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

    def reverseWords2(self, s: str) -> str:

        left, right = 0, len(s) - 1
        # 去掉字符串开头的空白字符
        while left <= right and s[left] == ' ':
            left += 1
        
        # 去掉字符串末尾的空白字符
        while left <= right and s[right] == ' ':
            right -= 1
            
        d, word = collections.deque(), []
        # 将单词 push 到队列的头部
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        d.appendleft(''.join(word))
        
        return ' '.join(d)



s = "I am a student"
s = " I am a student"
s = " I am     a student"
s1 = Solution()
print(s1.reverseWords(s))