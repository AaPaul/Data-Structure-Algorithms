'''
https://www.geeksforgeeks.org/count-subarrays-with-consecutive-elements-differing-by-1/

Examples: 
 
Input : arr[] = {1, 2, 3}
Output : 3
The subarrays are {1, 2}. {2, 3} and {1, 2, 3}

Input : arr[] = {1, 2, 3, 5, 6, 7}
Output : 6
'''
from typing import List
def subArr(arr: List[int]) -> int:
    l, r = 0, 0
    res = 0
    n = len(arr)
    for i in range(1, n):
        if arr[i] - arr[i-1] == 1:
            r += 1
        else:
            length = r - l + 1
            res += length * (length - 1)// 2
            l = r = i
    if l != r:
        length = r - l + 1
        res += length * (length - 1)// 2
    return res



arrs = [[1,2,3], [1,2,3,5,6,7]]
for arr in arrs:
    print(subArr(arr))