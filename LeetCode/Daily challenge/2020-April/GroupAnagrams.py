# Anagrams 字谜
from typing import List
import string

# The key point is to find that the word in the same group has common letters with same number
# 共同点就是组成该词的字母以及出现的次数相同，没有考虑出现次数测试用例4就会出错
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            i_sorted = ''.join(sorted(i)) # Using '' connect the elements in the list. so does '///'.join()
            if i_sorted not in res:
                res[i_sorted] = [] # Group words whose sequence fo the letter is same.
            res[i_sorted].append(i)
        print([res[k] for k in res.keys()])
        # return [res[k] for k in res.keys()]

            # d = dict.fromkeys(string.ascii_lowercase, 0) # create a dict including all letter

    def groupAnagrams_droped(self, strs: List[str]) -> List[List[str]]:
        def strToDict(s):
            _list = list(s)
            dic = {}
            for i in _list:
                if i not in dic.keys():
                    dic[i] = i
            return dic

        def isSame(dic_a: dict, dic_b: dict):
            if len(dic_a) != len(dic_b):
                return False
            for i in dic_a.keys():
                if i in dic_b.keys():
                    dic_b.pop(i)
            if dic_b:
                return False
            else:
                return True

        # def getIndex(strs:list, i:str):
        #     dict_index = dict(enumerate(strs))
        #     return (x for x in dict_index.keys() if dict_index[x] == i)

        count_list = []
        count = 0
        # value of range(list) will change synchronously and simultaneously if the list delete elements
        # for i in range(len(strs)):
        #     if strs[i] not in count_list:
        #         count_list.append([strs[i]])
        #         old_count = count
        #         count += 1
        #     dict_i = strToDict(strs[i])
        #     flag = 0
        #     for j in range(i+1, len(strs)-1, 1):
        #         if flag == 1:
        #             j -= 1
        #         dict_j = strToDict(strs[j])
        #         if isSame(dict_i, dict_j):
        #             # if strs[i] not in count_list:
        #             #     count_list[count].append(strs[i])
        #             count_list[old_count].append(strs[j])
        #             strs.remove(strs[j])
        #             flag = 1 # To check if the list delete an element

        for i in strs:
            if i not in count_list:
                count_list.append([i])
                old_count = count
                count += 1
            dict_i = strToDict(i)
            # index_i = getIndex(strs, i)
            index_i = strs.index(i)
            # flag = 0 # To prevent add the first element twice
            for j in strs[index_i+1:]:
                # these cannot work except for the first element
                # In the second loop, this statement can only miss the first element where we want the program miss second element as well
                # if flag == 0:
                #     flag = 1
                dict_j = strToDict(j)
                if isSame(dict_i, dict_j):
                    count_list[old_count].append(j)
                    index_j = strs[index_i + 1:].index(j) + (index_i + 1) # (index_i + 1) 是确定原列表中该元素(j)的位置
                    # strs.remove(j) # don't work
                    strs.pop(index_j)
                    # del j # work
        print(count_list)
        # return count_list


s1 = Solution()
s1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# s1.groupAnagrams(["", ""])
s1.groupAnagrams(["","a",""])
# s1.groupAnagrams(["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod","aha","nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"])


# Note: In for loop, we need to pay high attention on the case that if we want to remove the elements in the list
# Firstly, remove(i) function will remove the first element whose value is i，and the index() has the similar mechanism.
# Secondly, when we remove an element in list, the next element will replace the position of the removed element.
# In example 3, we want to remove the 3rd null element while the remove() function can only remove the first one.
# Therefore, the iteration will continue without dealing with "a" which is 1st element after removing "".
"""
list[:] is a copy of a list. （list.copy()）
list2 = list1
In fact, list1 and list2 share the common storage. They represent the same list.

"""

# Reference
# https://zhuanlan.zhihu.com/p/83807458