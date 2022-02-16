
'''
https://leetcode.com/discuss/interview-question/903219/alarmcom-new-grad-oa-2021-grouping-digits
https://medium.com/problem-solving-coding/grouping-digits-152457e961f8


Example
arr = [0, 1, 0, 1]
With 1 adjacent move, switching elements 1 and 2 yields [0, 0, 1, 1], a sorted array

arr = [1, 1, 1, 1, 0, 0, 0 0]
No need to move as it has been already grouped. Therefore, the order is not important.

'''
from typing import List


def groupDigits(nums: List[int]):
    n = len(nums)
    idx_p, elem_p = 0, nums[0]
    cnt = 0
    res0, res1 = 0, 0
    while cnt < n:
        elem_p = nums[cnt]
        if elem_p == 0:
            res0 += (cnt - idx_p)
            idx_p += 1
        cnt += 1
    idx_p = 0
    for i, elem_p in enumerate(nums):
        if elem_p == 1:
            res1 += (i - idx_p)
            idx_p += 1

    return min(res0, res1)

if __name__ == '__main__':

    nums = [1, 0, 0, 1]
    print(groupDigits(nums))


