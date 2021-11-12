from typing import List

def incrementBinaryNumber(numbers:str, request:List) -> List[int]:
    n = int(numbers, 2)
    add = int(1, 2)
    res = []
    for r in request:
        if r == '?':
            res.append(checkOne(n))
        # else:
        #     n = 
def test1(a, b):
    if (b == 0):
        return 1
    temp = test1(a, b // 2)
    if b%2 != 0:
        return temp*temp*a
    else:
        return temp * temp
# print(test1(3, 5))

def test2(a, b, c):
    res = 0
    while b > 0:
        res += (a%c) + (c%a)
        b -= a%c
        t = a
        a = c
        c = t
    return res
# print(test2(10, 25, 15))
def t3(a, b):
    while b > 0:
        a %= b
        t = a
        a = b
        b = t
    print(a)
t3(315, 840)

def sort1(strings):
    for i in range(len(strings)):
        for j in range(len())