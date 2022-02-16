'''


一个亚马逊用户评分数字list, 找有多少个decreasing sublist,
 这里decreasing 一定要是一分一分降的. 比如[4,3]就是3个,
一个4, 一个3, 一个[4,3]


https://leetcode.com/playground/P9doEn6x
'''

from typing import List

def decreasingSub(arr: List[int]) -> int:
    st = []
    count = 0
    for i in range(len(arr)):
        if st and st[-1] <= arr[i]:
            st.clear()
        st.append(arr[i])
        count += len(st)
    return count

print(decreasingSub([4, 3, 5, 4, 3]))
print(decreasingSub([4,4,3,5,3,4]))