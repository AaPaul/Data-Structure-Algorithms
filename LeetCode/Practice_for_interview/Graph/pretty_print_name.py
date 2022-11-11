# Google interview question
# https://www.youtube.com/watch?v=wjJiLpcAS6c
from collections import defaultdict


def fun(employees):
    # 1. build the graph
    graph = defaultdict(list)
    emp_mp = {}
    visiting = set()
    checked = set()
    stk = []

    for emp in employees:
        emp_mp[emp["id"]] = emp["name"]
        # graph[emp["id"]] = []
        if emp["managerId"] != emp["id"]:
            graph[emp["managerId"]].append(emp["id"])
    
    # topo sort
    def dfs(val):
        i, layer = val
        if i in checked:
            return False
        if i in visiting:
            return True
        visiting.add(i)
        # print(" " * layer + emp_mp[i])
        stk.append(val)
        for nei in graph[i]:
            res = dfs((nei, layer + 1))
            if res:
                return True

        checked.add(i)
        visiting.remove(i)
        return False
    
    for k in graph.keys():
        if k not in checked:
            res = dfs((k, 0))
            if res:
                print("Cycle detected")
                return 
    for i, layer in stk:
        print(" " * layer + emp_mp[i])
    





employees = [{ "id": 8, "managerId": 8, "name": "Alice" },
    { "id": 2, "managerId": 8, "name": "Bob" },
    { "id": 3, "managerId": 2, "name": "Emp3" },
    { "id": 4, "managerId": 3, "name": "Emp4" },
    { "id": 5, "managerId": 4, "name": "Emp5" },
    { "id": 6, "managerId": 3, "name": "Emp6" },
    { "id": 7, "managerId": 8, "name": "Emp7" }]

fun(employees)