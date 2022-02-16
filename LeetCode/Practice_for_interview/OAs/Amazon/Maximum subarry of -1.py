'''
Given an array of only 1 and -1, find a subarray of maximum length such that the product of all the elements in the subarray is 1
'''

from typing import List
def maxSub(arr:List[int]) -> List[int]:
    '''
    arr0: the idx of -1
    cnt: the number of -1
    '''
    arr0 = []
    cnt = 0
    for i, n in enumerate(arr):
        if n == -1:
            cnt += 1
            arr0.append(i)
    if cnt % 2 == 0:
        return arr
    # left to right
    i = 0
    l_cnt = 0
    r_cnt = 0
    while i < arr0[-1]:
        l_cnt += 1
        i += 1
    
    # right to left
    i = len(arr) - 1
    while i > arr0[0]:
        r_cnt += 1
        i -= 1
    return arr[:arr0[-1]] if l_cnt > r_cnt else arr[arr0[0]:]

print(maxSub([1, -1, 1, 1, -1, -1]))
print(maxSub([1, -1, 1, -1]))
