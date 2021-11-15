from typing import List
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        queriesPairs = []
        for i, q in enumerate(queries):
            queriesPairs.append([i, q])
        items.sort(key=lambda x:x[0])
        queriesPairs.sort(key=lambda x:x[1])
        
        maxBeauty = 0
        ans = [0] * len(queries)
        idx_item = 0
        for idx, q in queriesPairs:
            maxPrice = q
            while idx_item < len(items) and items[idx_item][0] <= maxPrice:
                maxBeauty = max(maxBeauty, items[idx_item][1])
                idx_item += 1
            ans[idx] = maxBeauty
        return ans

items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
queries = [1,2,3,4,5,6]

s = Solution()
print(s.maximumBeauty(items, queries))
