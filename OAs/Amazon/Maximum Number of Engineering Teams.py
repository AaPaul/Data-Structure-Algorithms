'''
https://leetcode.com/discuss/interview-question/1688196

Example1:
input: teamSize: 1, maxDiff: 1, skill: [34, 5, 72, 48, 15, 2]
output: 6 ---> (resulting teams [[2], [5], [15], [34], [48], [72]])

Example2:
input: teamSize: 3, maxDiff: 20, skill: [34, 5, 72, 48, 15, 2]
output: 1 ---> (resulting teams [[2, 5, 15]])
'''

from typing import List


def maxNum(teamSize: int, maxDiff: int, skill: List[int]):
    leastSkill = 0
    res = 0
    for i in range(len(skill)):
        while skill[i] - skill[leastSkill] > maxDiff:
            leastSkill += 1
        if i - leastSkill + 1 == teamSize:
            res += 1
            leastSkill = i + 1
    
    return res

if __name__ == "__main__":
    print(maxNum(1, 1, [34, 5, 72, 48, 15, 2]))
    print(maxNum(3, 20, [34, 5, 72, 48, 15, 2]))