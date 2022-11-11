
'''
16.21. Sum Swap LCCI: https://leetcode.cn/problems/sum-swap-lcci/
'''
def getPairs(a, b):
    sum_a, sum_b = sum(a), sum(b)
    ans = []
    for i in a:
        for j in b:
            if sum_a - i + j == sum_b - j + i:
                ans.append((i, j))

    return list(set(ans))

# s1 - n1 + n2 = s2 - n2 + n1 
# => s1 - s2 = 2(n1 + n2)
# => (s1 - s2) // 2 = n1 + n2
# -> (s1 - s2) is even

def getParis2(a, b):
    sum_a, sum_b = sum(a), sum(b)
    ans = []
    if (sum_a - sum_b) % 2:
        return ans
    diff = -(sum_a - sum_b) // 2

    mp = {b[i]: i for i in range(len(b))}
    print(mp, diff)
    for n in a:
        if diff + n in mp:
            ans.append((n, diff + n))
    return list(set(ans))

    


A = [4, 1, 2, 1, 1, 2]
B = [3, 6, 3, 3]
print(getPairs(A, B))
print(getParis2(A, B))