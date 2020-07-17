from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for i in nums:
            if i not in res:
                res[i] = 1
            else:
                res[i] += 1
        ans = []
        temp = sorted(res.items(), key= lambda item:item[1], reverse=True)
        for keys, values in temp:
            ans.append(keys)
            k-=1
            if not k:
                break
        return ans
s1 = Solution()
print(s1.topKFrequent([3,0,1,0], 1))


# Sort by Using keys
'''
items = dict.items()
items.sort()
for key,value in items:
   print key, value # print key,dict[key]
'''
# Sort in a Dictionary.
# We should transger it as an item and can use Sorted() function to finish the sorting part. This 
# function will return an ordered list including the elements in the dict. Note: the elements in the list
# are items instead of dictionary elements.

# What is lambda formular?

# Reference
# https://blog.csdn.net/wuguangbin1230/article/details/70174926