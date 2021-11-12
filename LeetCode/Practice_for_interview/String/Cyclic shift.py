"""
s = "abcd123" k = 3
Return "123abcd"
"""

def solution(s, k):
    n = len(s)
    k = k % n
    temp = s[n-k: n]
    # print(temp)
    print(temp+s[:n-k])

s = "abcd123"
k = 3
solution(s, k)