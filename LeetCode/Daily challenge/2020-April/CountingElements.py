from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr = sorted(arr)  # default:ascending order
        max_element = arr[-1]
        count = 0
        # lst = []
        # for i in range(len(arr)):
        for i in arr:
            if i + 1 in arr:
                # lst.append(i)
                count += 1
        print(count)
        # return count


s1 = Solution()
s1.countElements([1, 2, 3])
s1.countElements([1,1,3,3,5,5,7,7])
s1.countElements([1,1,2,2])
s1.countElements([1, 3, 2, 3, 5, 0])
