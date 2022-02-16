'''
https://leetcode.com/discuss/interview-question/1735633/Amazon-OA-2022

Example:
[1, 5, 4, 6, 8, 9, 2], k=3 (max diff)

res = 3
As:
[1,2],[5,4,6],[8,9]
'''

from typing import List

def grouping(videos: List[int], k: int) -> int:
    videos.sort()
    if len(videos) == 0:
        return 0
    # Should start from 1 as there would be at least 1 group
    res = 1
    idx = 0
    for i in range(len(videos)):
        if videos[i] - videos[idx] >= k:
            res += 1
            idx = i
    return res

if __name__ == "__main__":
    v = [1, 5, 4, 6, 8, 9, 2]
    print(grouping(v, 3))