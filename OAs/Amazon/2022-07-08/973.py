import heapq

from typing import List

def sol1(locations: List, delivers: int):
    def key(loc):
        x, y = loc
        return (x**2 + y**2, x)
    
    ans = heapq.nsmallest(delivers, locations, key=key)
    if len(ans) != delivers:
        return [[]]
    else:
        return ans

locations = [[1,2], [3,4], [1,-1]]
k =  2

# O(NlogK), O(N) to iterate all elements and logk to select the first k smallest element, k is the number of delivers

def sol2(locatioins, k):
    def qs()

print(sol1(locations, k))