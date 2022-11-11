'''
https://www.1point3acres.com/bbs/thread-937101-1-1.html
音乐会,总共n个人, 会给人与人之间的connection, 如果connection小与2就要离开, 问几小时之后就不会有人离开了。一个人离开之后,对应认识的人的connection也会减一
connection是给两个array, A和B, A index i 和B index i认识。
'''
from collections import defaultdict, deque


def fun(A, B, n):
    graph = defaultdict(list)
    indegree = [0] * n
    for i in range(len(A)):
        graph[A[i]].append(B[i])
        graph[B[i]].append(A[i])
        indegree[A[i]] += 1
        indegree[B[i]] += 1
    q = deque()
    for i in range(n):
        if indegree[i] < 2:
            q.append(i)
    count = 0
    while q:
        size = len(q)
        
        for i in range(size):
            t = q.popleft()
            indegree[t] = -1
            people = graph.get(t, None)
            if people is None:
                continue
            for p in people:
                indegree[p] -= 1
                if p not in q and -1 < indegree[p] < 2:
                    q.append(p)
        count += 1
    return count




A = [0, 0 ,1, 2]
B = [2, 3, 3, 3]
print(fun(A,B, 5))


#https://www.1point3acres.com/bbs/thread-910162-1-1.html

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