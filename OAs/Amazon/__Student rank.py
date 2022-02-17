'''
https://leetcode.com/discuss/interview-question/1741735/amazon-hackerrank-oa-sde-2-february-2022


'''
from typing import List

def stuRank(stu: List[int]) -> int:
    stu.sort(reverse=True)
    res = 0
    newArr = stu.copy()
