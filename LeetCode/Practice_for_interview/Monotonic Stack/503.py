
from typing import List


class Solution:
    # Cyclic case (circular array)
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # n_nums = nums + nums[:n-1]
        stk = []
        res = [-1] * n
        # for i in range(len(n_nums)):
        for i in range(2*n-1):
            while stk and nums[i % n] > nums[stk[-1]]:
                res[stk[-1]] = nums[i % n]
                stk.pop()
            stk.append(i % n)

        return res