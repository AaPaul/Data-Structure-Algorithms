from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        l_dict = {}
        for i in nums:
            if i not in l_dict:
                l_dict[i] = 1
            else:
                l_dict[i] += 1
        res = []
        for i,j in zip(l_dict.keys(), l_dict.values()):
            if j == 1:
                res.append(i)
        
        return res

    def singleNumber2(self, nums: List[int]) -> List[int]:
        ans = 0
        for num in nums:
            ans ^= num
            
        ans &= -ans
        res = [0] * 2
        
        for num in nums:
            if ans & num:
                res[0] ^= num
            else:
                res[1] ^= num
                
        return res


# list.count(list[i]) can calculate the number of the elements.