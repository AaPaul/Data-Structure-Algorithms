from typing import List
from math import ceil, floor

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # l = len(nums)
        # ans = [-1] * l
        
        # for i in range(l):
        #     if i < k:
        #         continue
        #     elif i == k:
        #         t = sum(nums[0:i]) + sum(nums[i:i+k+1])
        #         prev = 0
        #         cnt = 2 * k + 1
        #         # ans[i] = int(t / cnt)
        #         # ans[i] = floor(t / cnt)
        #         ans[i] = t // cnt
        #     else:
        #         if i + k >= l:
        #             break
        #         t = ans[i - 1] * cnt - nums[prev] + nums[i + k]
        #         # ans[i] = int(t / cnt)
        #         # ans[i] = floor(t / cnt)
        #         ans[i] = t // cnt

        #         prev += 1
        # return ans
        prefix = [0]
        for x in nums: prefix.append(prefix[-1] + x)
        
        ans = [-1]*len(nums)
        for i, x in enumerate(nums): 
            if k <= i < len(nums)-k: ans[i] = (prefix[i+k+1] - prefix[i-k])//(2*k+1)
        return ans 
                
# [0, 40527, 94223, 104953, 171444, 233585, 317494, 396129, 414689]
s1 = Solution()
nums = [40527,53696,10730,66491,62141,83909,78635,18560]
k = 2
# nums = [56725,48784,74934,6772,98570,96847,46483,6592,62552]
# k = 1
print(s1.getAverages(nums, k))


# class Solution:
#     def minimumDeletions(self, nums: List[int]) -> int:
#         # l_max, l_min = 1, 1
#         # r_max, r_min = 1, 1
#         n_max = -10 ** 6
#         n_min = -n_max
#         n = len(nums)
#         for i in range(n):
#             if nums[i] > n_max:
#                 n_max = nums[i]
#                 idx_max = i
#             if nums[i] < n_min:
#                 n_min = nums[i]
#                 idx_min = i
            
#         l_max = idx_max + 1
#         r_max = n - idx_max
#         l_min = idx_min + 1
#         r_min = n - idx_min
#         if idx_min == idx_max:
#             return min(l_max, r_max)
#         _sum = min(l_max, r_max) + min(r_min, l_min)
#         s_direction = min(max(l_max, l_min), max(r_max, r_min))
#         if _sum < s_direction:
#             return _sum
#         else:
#             return s_direction


# s1 = Solution()
# nums = [0,-4,19,1,8,-2,-3,5]


# print(s1.minimumDeletions(nums))



class TrieNode:
# Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:
def __init__(self):
    self.root = TrieNode()

def insert(self, word):
    current = self.root
    for letter in word:
        current = current.children[letter]
    current.is_word = True

def search(self, word):
    current = self.root
    for letter in word:
        current = current.children.get(letter)
        if current is None:
            return False
    return current.is_word

def startsWith(self, prefix):
    current = self.root
    for letter in prefix:
        current = current.children.get(letter)
        if current is None:
            return False
    return True