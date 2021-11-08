"""
The meaning of list[i:j] = [x]
if i == j, list[i:j] = [x] behaves like list.insert(j, x)
if i == j == len(list), list.append(x)
if i != j,  then slice of list from i to j is replaced by the contents of the iterable [x].


https://stackoverflow.com/questions/59060606/in-python-why-is-listii-n-insert-an-element-in-listii
"""
from typing import List




class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return []
        
        people.sort(key=lambda x:(-x[0], x[1]))
        ans = []
        for p in people:
            ans[p[1]:p[1]] = [p]

        return ans









