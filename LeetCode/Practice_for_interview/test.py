from typing import List

def incrementBinaryNumber(numbers:str, request:List) -> List[int]:
    n = int(numbers, 2)
    add = int(1, 2)
    res = []
    for r in request:
        if r == '?':
            res.append(checkOne(n))
        else:
            n = 
