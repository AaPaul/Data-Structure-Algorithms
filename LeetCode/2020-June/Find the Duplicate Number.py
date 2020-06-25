from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res_count = {}
        for i in nums:
            if i not in res_count.keys():
                res_count[i] = 1
            else:
                res_count[i] += 1
        for key, value in res_count.items():
            if value > 1:
                return key
