
from collections import defaultdict, deque
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        count = set()
        ans = 0
        q = deque()
        for i in nums:
            if len(q) < k:
                if i not in count:
                    q.append(i)
                    count.add(i)
                else:
                    # count.remove(i)
                    while q:
                        t = q.popleft()
                        if t == i:
                            break
                    q.append(i)

            else:
                ans = sum(q)
                if q[0] < i and (i not in count):
                    t = q.popleft()
                    ans += i - t
                    q.append(i)
                    count.remove(t)
                    count.add(i)
        return ans
        


# nums = [1,2,2]

# a = 2
print(Solution().maximumSubarraySum(nums=[3,5,3,4], k=2))


# def fun(arr):
#     for prod in arr:
#         idx = prod["id"]
#         name = prod["name"]
#         comp = prod.get("manufacturer", None)
#         price = prod["price"]
#         if comp is None:
#             print("Product {0} has price {1} and no manufacturer".format(name, price))
#         else:
#             print("Product {0} has price {1} and manufacturer {2}".format(name, price, comp))




# arr = [
#     {
#         "id" : 1,
#         "name" : "pname1",
#         "updated_at" : 15000,
#         "price" : 100,
#         "manufacturer" : "Company1"
#     },
#     {
#         "id" : 2,
#         "name" : "pname2",
#         "updated_at" : 15230,
#         "price" : 90,
#     }
# ]

# fun(arr)