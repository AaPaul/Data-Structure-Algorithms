'''
https://leetcode.com/discuss/interview-question/1488281/Amazon-OA

'0': an ordinary page
'1': a bookmarked page

Find the number of ways to select 3 pages in ascending index order such that no two adjacent selected pages are of the same type.

Example

book = '01001'

The following sequences of pages match the criterion:

[1, 2 ,3], that is, 01001 → 010.
[1, 2 ,4], that is, 01001 → 010.
[2, 3 ,5], that is, 01001 → 101.
[2, 4 ,5], that is, 01001 → 101.

The answer is 4.
'''

from collections import Counter


def numberOfWays(book: str) -> int:
    left = {'0': 0, '1': 0}
    right = Counter(book)
    ans = 0
    for c in book:
        right[c] -= 1
        if c == '1':
            ans += left['0'] * right['0']
        else:
            ans += left['1'] * right['1']
        left[c] += 1
    return ans

print(numberOfWays('01001'))
print(numberOfWays('10111'))
print(numberOfWays('0001'))