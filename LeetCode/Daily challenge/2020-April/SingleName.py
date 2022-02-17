from typing import List
from collections import Counter
import pandas as pd
class solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict1 = {}
        for i in nums:
            dict1[i] = dict1.get(i, 0) + 1
        min = list(dict1.values())[0]
        min_key = 0
        for i in dict1:
            if dict1[i] <= min:
                min = dict1[i]
                min_key = i
        return min_key

    # Using collection package
    def method2(self, nums: List[int]) -> int:
        dict1 = Counter(nums)
        dict1 = dict(dict1)

    # Using Pandas
    def method3(self, nums:List[int]) -> int:
        dict1 = pd.value_counts(nums)
        dict1 = dict(dict1)

def main():
    s1 = solution()
    print(s1.singleNumber([4,1,2,1,2]))


if __name__ == "__main__":
    main()


# local variable 'min_key' referenced before assignment
'''
If we don't state 'min_key' before we use it. The program may be confused whether
the variable is just used in the loop or in the whole function.
'''