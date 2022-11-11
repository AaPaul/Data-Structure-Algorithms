'''
https://liuzhenglaichn.gitbook.io/algorithm/monotonic-stack

Decreasing monotonic stack means: stk[5, 4, 2, 1], if we want to push 3 into the stack,
we need to pop [1, 2] so that we can keep the decreasing order.
'''

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk = []
        n = len(nums2)
        tmp = [0] * n
        for i in range(n-1, -1, -1):
            while stk and nums2[i] <= stk[-1]:
                stk.pop()
            if not stk:
                tmp[i] = -1
            else:
                tmp[i] = stk[-1]
            stk.append(nums2[i])
        
        mp = {}
        for i in range(n):
            mp[nums2[i]] = tmp[i]
        
        res = [0] * len(nums1)
        for i in range(len(nums1)):
            res[i] = mp[nums1[i]]
        return res
#         for i in range(len(nums2)-1, -1, -1):
#             while stk and nums2[i] >= stk[-1]:
#                 stk.pop()
#             if not stk:
#                 tmp[i] = -1
#             else:
#                 tmp[i] = stk[-1]
#             stk.append(nums2[i])
        
#         mp = {}
#         for i in range(n):
#             mp[nums2[i]] = tmp[i]
        
#         # res = []
#         # for i in range(len(nums1)):
#         #     res.append(mp[nums1[i]])
#         res = [0] * len(nums1)
#         for i in range(len(nums1)):
#             res[i] = mp[nums1[i]]
            
        
#         return res
        