# To find an subarray where the number of 1 and 0 are the same.

from typing import List


class Solution:
    # The application of hashmap
    # In python, dict can be seen as the hashmap structure in Java.
    def findMaxLength(self, nums: List[int]) -> int:
        index_dict = {0: -1}
        sum = 0
        max_len = 0

        # The first use of function enumerate on list. i is the indices and num is the value in the list.
        for i, num in enumerate(nums):
            if num == 0:
                sum -= 1
            else:
                sum += 1
            if sum in index_dict:
                max_len = max(max_len, i - index_dict[sum])
            else:
                index_dict[sum] = i
        print(max_len)
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         sum -= 1
        #     else:
        #         sum += 1
        #     if sum in index_dict:
        #         max_len = max(max_len, i - index_dict[sum])
        #     else:
        #         index_dict[sum] = i
        # print(max_len)

    # Time limit exceeded
    def findMaxLength1(self, nums: List[int]) -> int:

        max_len = 0
        if not nums:
            return 0
        for j in range(len(nums)):
            sum = 0
            for i in range(j, len(nums)):
                if nums[i] == 0:
                    sum -= 1
                else:
                    sum += 1
                if sum == 0:
                    if max_len < i - j:
                        max_len = i - j + 1
                        start = i
                        end = j

        # return max_len
        print(max_len)


s1 = Solution()
s1.findMaxLength([0, 1, 1, 1, 0, 1, 1, 1, 1, 0])
s1.findMaxLength([0, 1, 1, 1, 0, 0])
