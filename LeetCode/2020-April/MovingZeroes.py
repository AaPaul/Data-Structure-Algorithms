from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        length = len(nums)
        i = 0
        # The reason why not use for() is that we want to control the change of i and the number of loop
        # Another mistake. Consider exception like [0]
        # Another one again. [0, 0, 0]
        while i < length:
            if nums[i] == 0:
                nums.pop(i)
                count += 1
                length -= 1
                if length == 0:
                    break
                # Actually, this the reason why I'm wrong in the 2nd problem. It's an extra and useless statement.
                # No need to change i if we meet a zero. Keep the orginal value.
                # else:
                #     i-=1
            else:
                i += 1
        for i in range(count):
            nums.append(0)
        # return nums


# s1 = Solution()
# l = s1.moveZeroes([0, 0, 1])
# l = s1.moveZeroes([0])
# l = s1.moveZeroes([0, 0 , 0])
# print(l)
