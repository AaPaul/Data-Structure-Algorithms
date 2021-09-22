# 88. Merge Sorted Array
from typing import List

# This question asks us to start from the rare as the value would be replaced if 
# we start from the first.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx_1, idx_2 = m - 1, n - 1
        idx_merged = len(nums1) - 1

        while idx_merged >= 0:
            if idx_1 < 0:
                nums1[idx_merged] = nums2[idx_2]
                idx_2 -= 1
            elif idx_2 < 0:
                nums1[idx_merged] = nums1[idx_1]
                idx_1 -= 1
            elif nums1[idx_1] > nums2[idx_2]:
                nums1[idx_merged] = nums1[idx_1]
                idx_1 -= 1
            else:
                nums1[idx_merged] = nums2[idx_2]
                idx_2 -= 1
            idx_merged -= 1

if __name__ == "__main__":
    s1 = Solution()
    nums1 = [-1,3,0,0,0,0,0]
    m = 2
    nums2 = [0,0,1,2,3]
    n = 5
    s1.merge(nums1, m, nums2, n)
    print(nums1)
